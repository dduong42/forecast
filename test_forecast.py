import json
import unittest

from forecast import (
    formated_date_from_timestamp,
    InformationGetter,
)


def test_formated_date_from_timestamp():
    assert formated_date_from_timestamp(1410800400) == '2014-09-15'
    assert formated_date_from_timestamp(1411923600) == '2014-09-28'


class TestInformationGetter(unittest.TestCase):
    def setUp(self):
        f = open('london.json')
        d = json.loads(f.read())
        l = d['list']
        self.info_getter = InformationGetter(l)

    def test_list_min(self):
        assert self.info_getter.get_list_min() == [
            53.74, 49.08, 49.75, 41.11, 42.73, 60.84,
            61.54, 65.57, 54.48, 53.46, 50.22, 54.84,
            47.12, 45.55,
        ]

    def test_list_max(self):
        assert self.info_getter.get_list_max() == [
            62.2, 60.22, 63.48, 53.67, 61.12, 68.76,
            71.19, 74.75, 73.74, 70.12, 53.29, 62.55,
            56.19, 57.74,
        ]

    def test_forecasts(self):
        assert self.info_getter.get_forecasts() == {
            'Rain': ['2014-09-15', '2014-09-18', '2014-09-20', '2014-09-21',
                     '2014-09-22', '2014-09-23', '2014-09-24', '2014-09-25',
                     '2014-09-26', '2014-09-27', '2014-09-28'],
            'Clouds': ['2014-09-16'],
            'Clear': ['2014-09-17', '2014-09-19']
        }

    def test_summary(self):
        assert self.info_getter.get_summary('London') == {
            'city': 'London',
            'max': 74.75,
            'min': 41.11,
            'forecasts': {
                'Rain': ['2014-09-15', '2014-09-18', '2014-09-20',
                         '2014-09-21', '2014-09-22', '2014-09-23',
                         '2014-09-24', '2014-09-25', '2014-09-26',
                         '2014-09-27', '2014-09-28'],
                'Clouds': ['2014-09-16'],
                'Clear': ['2014-09-17', '2014-09-19']
            }
        }
