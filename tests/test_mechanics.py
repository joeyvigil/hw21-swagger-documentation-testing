from app import create_app
from app.models import Mechanics, db
import unittest
from werkzeug.security import check_password_hash, generate_password_hash
from app.util.auth import encode_token


#Run Script: python -m unittest discover tests

class TestMechanics(unittest.TestCase):

    #Runs before each test_method
    def setUp(self): 
        self.app = create_app('TestingConfig') #Create a testing version of my app for these testcases
        self.mechanic = Mechanics(password=generate_password_hash('password123'), first_name = 'Jon', last_name = 'doe', email = 'john@doe.com', salary = 100, address = '123 main street') #Creating a starter mechanic, to test things like get, login, update, and delete
        with self.app.app_context(): 
            db.drop_all() #removing any lingering table
            db.create_all() #creating fresh for another round of testing
            db.session.add(self.mechanic)
            db.session.commit()
        self.token = encode_token(1) #encoding a token for my starter Mechanic defined above ^
        self.client = self.app.test_client() #creates a test client that will send requests to our API

    
    #test creating a mechanic (IMPORTANT all test functions need to start with test)
    def test_create_mechanic(self):
        mechanic_payload = {
            "first_name": "jane",
            "last_name": "doe",
            "email": "jane@doe.com",
            "password": "password123",
            "salary": 100.0,
            "address": "123 main street"
        }


        response = self.client.post('/mechanics', json=mechanic_payload) #sending a test POST request using our test_client, and including the JSON body
        print(response.json)
        self.assertEqual(response.status_code, 200) #checking if I got a 201 status
        self.assertEqual(response.json['first_name'], "jane") #Checking to make sure the data that I sent in, is apart of the response.
        self.assertTrue(check_password_hash(response.json['password'], "password123"))


    #Negative check: See what happens when we intentially try and break an endpoint
    def test_invalid_create(self):
        mechanic_payload = {
            "first_name": "jane",
            "last_name": "doe",
            "password": "password123",
            "salary": 100.0,
            "address": "123 main street"
        }

  
        response = self.client.post('/mechanics', json=mechanic_payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn('email', response.json) #Membership check that email is in the response json

    def test_nonunique_email(self):
        mechanic_payload = {
            "first_name": "jon",
            "last_name": "doe",
            "email": "jon@doe.com",
            "password": "password123",
            "salary": 100.0,
            "address": "123 main street"
        }

        response = self.client.post('/mechanics', json=mechanic_payload)
        self.assertEqual(response.status_code, 500)


    def test_get_mechanics(self):
    
        response = self.client.get('/mechanics')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[0]['first_name'], 'jon')

    def test_login(self):
        login_creds = {
            "email": "jon@doe.com",
            "password": "password123"
        }

        response = self.client.post('/mechanics/login', json=login_creds)
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json)


    def test_delete(self):
        headers = {"Authorization": self.token}

        response = self.client.delete("/mechanics/1", headers=headers) #Sending delete request to /mechanics with my Authorization headers
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Successfully deleted mechanic 1')


    def test_unauthorized_delete(self):

        response = self.client.delete("/mechanics/1") #Sending delete request to /mechanics without token
        self.assertEqual(response.status_code, 401) #Should get an error response

    
    def test_update(self):
        headers = {"Authorization": self.token}

        update_payload = {
            "first_name": "jom",
            "last_name": "doe",
            "email": "NEW_EMAIL@email.com",
            "password": "password123",
            "salary": 110.0,
            "address": "123 main street"
        }

        response = self.client.put('/mechanics/1', headers=headers, json=update_payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['first_name'], 'NEW_EMAIL@email.com')




       

    
   

 

