print('Тестируем апликуху!')
import os
from os import listdir
from os.path import isfile, join
import json
import requests
import unittest
BASE_SERVER = 'http://flask:5000/'

class TestByJsonFiles(unittest.TestCase):
    def setUp(self):
        print('Setting up')

    def test_all_json(self):
        jsonfiles = [f for f in listdir('json') if isfile(join('json', f))]
        for j in jsonfiles:
            with open(os.path.join('json',j),'r') as file:
                tasks = json.loads(file.read())

            for task in tasks:  
                print(task['name'])
                if task["request"]["type"] == 'POST':
                    url = f'{BASE_SERVER}{task["request"]["url"]}'
                    data = task["request"]["data"]
                    headers = task["request"]["header"]
                    r = requests.post(url,data=data,headers=headers)
                    resp = json.loads(r.text)
                    print(task["response"])
                    for checking in task["response"]:
                        if checking["type"] == 'assertIn':
                            #print(checking)
                            self.assertEqual(checking["data"][0],checking["data"][1])
