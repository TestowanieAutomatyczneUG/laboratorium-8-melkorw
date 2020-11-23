import requests


resp = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata")

print(resp.json()['meals'])