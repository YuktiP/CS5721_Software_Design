import os
import sys
sys.path.append('C:/Users/RRL/Project/CS5721_Software_Design/')
from app import app,db
from flask import Flask

import unittest


class Test_AdminDashboard(unittest.TestCase):

    #def __init__(self):
     #   self = self
    

    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()
        self._ctx = self.app.test_request_context()
        self._ctx.push()


    def test0_login_user(self):
        print("******Running test case 1 to check whether admin user is logged in******")
        response = self.client.get('/login', content_type = 'html/text')
        self.assertEqual(response.status_code,200,'Unable to load login page.' +str(response.status_code)+' was returned')
        with self.client:
            response_post_login = self.client.post('/login', data = dict(email="test@test.com",password="password",submit="submit"),follow_redirects=True)
            self.assertEqual(response_post_login.status_code,200,'Unable to load login page.' +str(response_post_login.status_code)+' was returned')


    def test1_admin_route(self):
        self.test0_login_user()
        print("******Running test case 1 to check whether admin route is running correctly******")
        response = self.client.get('/showrequests', content_type = 'html/text')
        self.assertEqual(response.status_code,200,'Response code is not 200. Instead '+str(response.status_code)+' was returned')


    def test2_admin_page_loads(self):
        self.test0_login_user()
        print("******Running test case 2 to check whether admin page is loading correctly******")
        response = self.client.get('/showrequests', content_type = 'html/text')
        self.assertTrue(b'Welcome Admin' in response.data)
    


if __name__ == "__main__":
    unittest.main()