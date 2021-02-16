print('Тестируем апликуху!')
import os
from os import listdir
from os.path import isfile, join
from util import test_json
import json
import unittest


class TestCreateDriver(unittest.TestCase):

    def test_create_driver(self):
        with open(os.path.join('json','create-driver.json'),'r') as file:
            tasks = json.loads(file.read())
        test_json(tasks)

  