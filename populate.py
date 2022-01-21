
from numbers_api.models import Number



def create_objects(ordered_array):

    for n in range(0, len(ordered_array)-99, 100):
        obj = Number.objects.create(number = ordered_array[n:n+100])
        obj.save()


