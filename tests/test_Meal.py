import unittest
from src.meal.meal import Meal


class TestMeal(unittest.TestCase):
    def tearUp(self):
        self.temp = Meal()
    def test_get_meal(self):
        response = self.temp.get_meal('Arrabiata')
        self.assertEqual('52771', response['meals']['idMeal'])