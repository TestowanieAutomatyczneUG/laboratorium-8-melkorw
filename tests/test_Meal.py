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

    def test_get_meal_with_id(self):
        self.assertEqual('52771', self.temp.get_meal(
            'Arrabiata', 0)['idMeal'])

    def test_get_meal_with_not_existing_id(self):
        self.assertEqual('There is no meal with given ID', self.temp.get_meal(
            'Arrabiata', 2))

    def test_get_meal_not_existing_meal(self):
        self.assertEqual('Meal does not exist', self.temp.get_meal(
            'Arrabiatass', 2))

    def tearDown(self):
        self.temp = None
