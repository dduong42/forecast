import datetime
import requests

API_URL = 'http://api.openweathermap.org/data/2.5/forecast/daily'


def formated_date_from_timestamp(timestamp):
    "Takes a timestamp and returns a date in this format: yyyy-mm-dd"

    t = datetime.datetime.fromtimestamp(timestamp)
    return t.strftime('%Y-%m-%d')


class InformationGetter(object):
    "Gets misc info from the list"

    def __init__(self, l):
        self.l = l

    def get_list_min(self):
        "Returns the list of min temperatures"

        return [el['temp']['min'] for el in self.l]

    def get_list_max(self):
        "Returns the list of max temperatures"

        return [el['temp']['max'] for el in self.l]

    def get_forecasts(self):
        "Returns the forecast dict"

        d = {}
        for el in self.l:
            weather = el['weather'][0]['main']
            formated_date = formated_date_from_timestamp(el['dt'])
            try:
                d[weather].append(formated_date)
            except KeyError:
                d[weather] = [formated_date]
        return d

    def get_summary(self, city):
        "Returns the forecast summary dict"

        return {
            'city': city,
            'max': max(self.get_list_max()),
            'min': min(self.get_list_min()),
            'forecasts': self.get_forecasts()
        }


def summarise_forecast(city):
    "Returns the forecast summary for a city"

    r = requests.get(API_URL, params={'q': city, 'units': 'imperial',
                     'cnt': 14})
    d = r.json()
    info_getter = InformationGetter(d['list'])
    return info_getter.get_summary(city)


if __name__ == "__main__":
    print summarise_forecast('Paris')
