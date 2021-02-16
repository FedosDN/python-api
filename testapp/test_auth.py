print('Тестируем апликуху!')
import os
from os import listdir
from os.path import isfile, join
from util import test_json
import json
import unittest


class TestAuth(unittest.TestCase):
    def setUp(self):
        print('Setting up')


    def test_auth(self):
        with open(os.path.join('json','auth.json'),'r') as file:
            tasks = json.loads(file.read())
        test_json(tasks)
               
        # jsonfiles = [f for f in listdir('json') if isfile(join('json', f))]
        # for j in jsonfiles:
        #     with open(os.path.join('json',j),'r') as file:
        #         tasks = json.loads(file.read())
        #     test_json(tasks)