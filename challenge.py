
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()
import asyncio
from aiohttp import ClientSession
import sorting_script
import populate

page=1 # Variable that stores the page number to be requested
urls = [] # Array with all the endpoints
url = "http://challenge.dienekes.com.br/api/numbers?page={}" 
aux_number_list = [] # Auxiliary variable that stores all the numbers but also the errors and empty lists
number_list = [] # List that will store all the numbers obtained from the requests


# This function does the get requests to 
# the received url and returns the data obtained
async def get_data(url, session):
    req = await session.request(method="GET", url=url)
    json = await req.json() # get the json content from the request
    if req.status == 200:  # if it's not a simulated error, returns the array (empty or with numbers), if any other status code, returns None
        return json['numbers']


# This function creates an array called tasks 
# that stores all the requests to be done
# in parallel
async def make_requests(urls):
    async with ClientSession() as session:
        tasks = []
        for url in urls: # iterave over the urls and adds each task to the tasks array
            tasks.append(get_data(url=url, session=session))
        aux_number_list.extend(await asyncio.gather(*tasks)) #Stores all the returned data from the requests on aux_number_list

print("Making the GET requests to the API...")

# This loop will run until an empty list is detected on the jsons received.
while True:
    urls.append(url.format(page)) # Creates a list of urls to make all the requests simultaneously.
    page += 1

    # Once the number of pages becomes a multiple of 6000, the requests are made.
    # This means that the requests are made in batches of 6000 each time.

    # This number was chosen because the requests must be made asynchronously
    # in order to save time, but it is also necessary to stop making these requests
    # once we receive and empty array. Since it is known that the last page is 10000,
    # 6000 is a good number that keeps the balance between time efficiency and 
    # fewer pointless requests that only returns empty arrays. 

    # Even though this method requires that a number is defined, it ends the process
    # when the end is actually detected and not hardcoded, so we dont really need
    # to know when the endpoints ends and the process is finished automatically.

    # If we decrease this number, it would take more time to end the process
    # but less requests with empty results would be made. On the contrary,
    # if the number is increased, the whole process would be faster (depending on
    # how much is it incresed) but the number of requests with empty results would
    # be increased. 
    
    if (page % 6000 == 0):  
        asyncio.run(make_requests(urls))
        urls = []  # Refreshes the url list
    if [] in aux_number_list: # if any empty array is detected, the loop is stopped.
        break

#This loop cleans the result array from empty arrays received at the end
# and None objects that are stored when an error is received
for n in aux_number_list:
    if n not in ([], None):
    #if n != [] and n != None:
        number_list.extend(n)

print(f"Requests finished. {len(number_list)} numbers were obtained.")
print("Ordering numbers...")

ordered_number_list = sorting_script.run(number_list)

print("Ordering finished.")
print("Creating objects on the database...")

populate.create_objects(ordered_number_list)

print("Process finished.")


