import unittest
from src.meal.meal import Meal


class TestMeal(unittest.TestCase):
    def setUp(self):
        self.temp = Meal()

    def test_get_meals(self):
        response = self.temp.get_meals('Arrabiata')
        self.assertEqual(1, len(response))

    def tearDown(self):
        self.temp = None
