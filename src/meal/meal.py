import requests


class Meal:
    def get_meals(self, name):
        mydict = {'s': name}
        resp = requests.get('https://www.themealdb.com/api/json/v1/1/search'
                            '.php', params=mydict)
        if resp.json()['meals'] is None:
            return 'Meal does not exist'
        return resp.json()['meals']

    def get_meal(self, name, meal_id):
        mydict = {'s': name}
        resp = requests.get('https://www.themealdb.com/api/json/v1/1/search'
                            '.php', params=mydict)
        if resp.json()['meals'] is None:
            return 'Meal does not exist'

        if meal_id < 0 or meal_id > len(resp.json()['meals']):
            return 'There is no meal with given ID'
        return resp.json()['meals'][meal_id]