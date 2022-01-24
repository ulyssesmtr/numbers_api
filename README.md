# How to install and run

## Linux:

###### 1. Download the zip and extract it to the desired folder.

###### 2. Open the terminal at the project folder and run the following command:

      python3 -m venv venv

   This will create a virtual environment at the project folder called venv.
   Python must be installed. Preferably version 3.9 but any close version should work fine.

###### 3. Activate the virtual environment by running the following command at the project folder:

      $ source venv/bin/activate

   Make sure that you are on the folder where the file manage.py is located in order to run the next commands.

###### 4. Install the requirements by running the following command:

        pip install -r requirements.txt

###### 5. Create the database by running:

        python manage.py migrate

###### 6. Run the challenge.py file in order to make the requests, sort the numbers and populate the database.
 
        python challenge.py

   This process may take a few seconds.

###### 7. Start the server by runnning the following command:

        python manage.py runserver

## Windows:

###### 1. Download the zip and extract it to the desired folder.

###### 2. Open the project folder with the terminal and and run the following command:

        py -3.9 -m venv venv

   This will create a virtual environment at the project folder called venv.
   Python must be installed. Preferably version 3.9 but any close version should work fine.

###### 3. Activate the virtual environment by running the following command:

        absolute_path\numbers_api-main\venv\Scripts\Activate.ps1 (if CLI is Windows Powershell)

        absolute_path\numbers_api-main\venv\Scripts\activate.bat (if cmd.exe)

 Make sure that you are on the folder where the file manage.py is located in order to run the next commands.
 
###### 4. Install the requirements by running the following command:

        pip install -r requirements.txt

###### 5. Create the database by running:

        python manage.py migrate

###### 6. Run the challenge.py file in order to make the requests, sort the numbers and populate the database.

        python challenge.py

   This process may take a few seconds.

###### 7. Start the server by runnning the following command:

        python manage.py runserver


# API

After starting the server, access localhost:8000/ and it will show the numbers/ endpoint.
This endpoint returns the first list of 100 ordered numbers, and also
the link for the next endpoint.
Every array can be requested by the following endpoints:

###### http://localhost:8000/numbers/{int} -> int is the object id

###### http://localhost:8000/numbers/?offset={int} -> int is page number, every page returns only one array.

###### http://localhost:8000/numbers/?limit={x}&offset={int} -> int is the page number and x is the number of arrays returned from this endpoint, starting from int

The sorting is done from smallest to largest, so the first endpoint:
###### http://localhost:8000/numbers/1
will contain the array with the 100 smallest numbers, and the last endpoint:
###### http://localhost:8000/numbers/{int} -> int depends on how many requests were successfull during the execution of challenge.py
will contain the array with the 100 largest numbers.

The documentation is also available at http://localhost:8000/doc

Tests can be executed by the following command:

python manage.py test

The tests file is located at numbers_api/tests.py
