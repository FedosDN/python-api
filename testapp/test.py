print('Тестируем апликуху!')
import os
from os import listdir
from os.path import isfile, join
import json
import requests
import unittest
BASE_SERVER = 'http://flask:5000/'

def check_status(resp):
    print(resp)
    if resp.status_code != 200:
        with open('response_page.html', 'w') as f:
            f.write(resp.text)

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
                url = f'{BASE_SERVER}{task["request"]["url"]}'
                if task["request"]["type"] == 'POST':
                    
                    data = task["request"]["data"]
                    headers = task["request"]["header"]
                    r = requests.post(url,data=data,headers=headers)
                    print(r.text)
                    resp = json.loads(r.text)
                    #print(task["response"])
                    for checking in task["response"]:
                        if checking["type"] == 'assertIn':
                            #print(checking)
                            self.assertIn(checking["data"],resp)

                        if checking["type"] == 'assertEqual':
                            #print(checking)
                            self.assertEqual(checking["data"][0],checking["data"][1])

                if task["request"]["type"] == 'GET':
                    headers = task["request"]["header"]
                    r = requests.get(url,headers=headers)
                    check_status(r)
                    resp = json.loads(r.text)
                    #print(resp)
                    for checking in task["response"]:
                        if checking["type"] == 'assertIn':
                            #print(checking)
                            self.assertIn(checking["data"],resp)

                        if checking["type"] == 'assertEqual':
                            #print(checking)
                            self.assertEqual(resp[checking["data"][0]],checking["data"][1])
