import requests


class Meal:
    def get_meals(self, name):
        mydict = {'s': name}
        resp = requests.get('https://www.themealdb.com/api/json/v1/1/search'
                            '.php', params=mydict)
        if resp.json()['meals'] is None:
            return 'Meal does not exist'
        return resp.json()['meals']


