import os
import sys
sys.path.append("C:/Users/RRL/Project/CS5721_Software_Design/")
from flask import Flask,request
from app import app,db
import unittest

class Test_UnblockCardPage(unittest.TestCase):

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
        print("******Checking login before the start of testcases******")
        response = self.client.get('/login', content_type = 'html/text')
        self.assertEqual(response.status_code,200,'Unable to load login page.' +str(response.status_code)+' was returned')
        with self.client:
            response_post_login = self.client.post('/login', data = dict(email="test@test.com",password="password",submit="submit"),follow_redirects=True)
            self.assertEqual(response_post_login.status_code,200,'Unable to load login page.' +str(response_post_login.status_code)+' was returned')

    def test1_unblock_route(self):
        self.test0_login_user()
        print("******Running test case 2 to check whether unblock route is running correctly******")
        response = self.client.get('/unblock', content_type = 'html/text')
        self.assertEqual(response.status_code,200,'Response code is not 200. Instead '+str(response.status_code)+' was returned')
        self.assertTrue(b'Requests to Unblock Card' in response.data, 'Unable to see the unblock card data')

        
    
    def test2_unblock_card(self):
        self.test0_login_user()
        print("******Running test case 3 to check whether unblock card makes the card active again******")
        data_button_1 = {'add':1234}
        data_button_2 = {'add':12345}
        self.client.post('/unblock', data = data_button_1)
        response = self.client.get('/unblock', follow_redirects=True)
        self.assertTrue(b'The Card has been unblocked successfully' in response.data)
        self.client.post('/unblock', data = data_button_2)
        response_1 = self.client.get('/unblock', follow_redirects=True)
        self.assertTrue(b'The Card has been unblocked successfully' in response_1.data)
        self.assertTrue(b'No cards to unblock' in response_1.data)

    
if __name__ == "__main__":
    unittest.main()