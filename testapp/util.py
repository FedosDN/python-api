import requests
BASE_SERVER = 'http://flask:5000/'
import json
import unittest
tc = unittest.TestCase()

def check_status(resp):
    print(resp)
    if resp.status_code != 200:
        with open('response_page.html', 'w') as f:
            f.write(resp.text)

def test_json(tasks):
    for task in tasks:  
        print(task['name'])
        url = f'{BASE_SERVER}{task["request"]["url"]}'
        if task["request"]["type"] == 'POST':
            
            data = task["request"]["data"]
            headers = task["request"]["header"]
            r = requests.post(url,data=data,headers=headers)
            print(r.text)
            resp = json.loads(r.text)
            print(task["response"])
            for checking in task["response"]:
                if checking["type"] == 'assertIn':
                    #print(checking)
                    tc.assertIn(checking["data"],resp)

                if checking["type"] == 'assertEqual':
                    #print(checking)
                    tc.assertEqual(checking["data"][0],checking["data"][1])

        if task["request"]["type"] == 'GET':
            headers = task["request"]["header"]
            r = requests.get(url,headers=headers)
            check_status(r)
            resp = json.loads(r.text)
            #print(resp)
            for checking in task["response"]:
                if checking["type"] == 'assertIn':
                    #print(checking)
                    tc.assertIn(checking["data"],resp)

                if checking["type"] == 'assertEqual':
                    #print(checking)
                    tc.assertEqual(resp[checking["data"][0]],checking["data"][1])
