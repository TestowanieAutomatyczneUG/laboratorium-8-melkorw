import requests
from src.meal.meal import Meal

resp = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata")



meal = Meal()
resp = meal.get_meal('Arrabiata')
print(resp['meals'])