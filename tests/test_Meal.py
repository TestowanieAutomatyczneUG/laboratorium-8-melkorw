import unittest
from src.meal.meal import Meal


class TestMeal(unittest.TestCase):
    def setUp(self):
        self.temp = Meal()

    def test_get_meals(self):
        response = self.temp.get_meals('Arrabiata')
        self.assertEqual(1, len(response))

    def test_get_meals_null(self):
        response = self.temp.get_meals('Arrabiatas')
        self.assertEqual('Meal does not exist', response)


    def tearDown(self):
        self.temp = None
