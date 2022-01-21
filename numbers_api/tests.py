from django.test import TestCase
import sorting_script
import populate
from numbers_api.models import Number

class ChallengeTestCase(TestCase):

    def setUp(self):
        self.array = [9, 3, 5, 2, 4, 1, 6, 8, 7]
        self.ordered_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        array = [n for n in range(100)]
        self.number_obj = populate.create_objects(array)

    def test_ordering_algorithm(self):
        """
        Tests if the sorting algorithm works
        """
        self.assertEqual(sorting_script.run(self.array), self.ordered_array)

    def test_populate_script_return(self):
        """
        Tests if the populate script returns None
        """
        self.assertIsNone(self.number_obj)

    def test_populate_script(self):
        """
        Tests if the populate script creates an object correctly.
        """
        self.assertIsNotNone(Number.objects.all())
        self.assertIsInstance(Number.objects.get(id=1).number, list)

    def test_populate_script_quantity(self):
        """
        Tests if the populate script creates exactly one object.
        """
        self.assertEqual(len(Number.objects.all()), 1)

