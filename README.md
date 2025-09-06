# hw21-swagger-documentation-testing
Utilizing Flask-Swagger and Flask-Swagger-UI Document Each Route of your API

## Documentation
Utilizing Flask-Swagger and Flask-Swagger-UI Document Each Route of your API. Each Route Requires:

Path:

-   Endpoint
-   Type of request (post, get, put, delete)
-   tag (category for the route)
-   summary
-   description
-   security: Points to the security definition (Only need this for token authenticated routes)
-   parameters: Information about what the data the route requires(Note: Some Routes don't have parameters)
-   responses: Information about what the data  route returns (Should include examples)

**Note:** We did not cover how to document Query or Path parameters, I want you guys to figure this out for yourselves. As a developer you'll need to be comfortable searching for info on your own.
Definition(s):

-   PayloadDefinition: Defines the "Shape" of the incoming data 
-   ResponseDefinitions: Defines the "Shape" of the outgoing data 

## Testing

Utilizing the built-in unittest library:

-   Create a tests folder inside you project folder
-   Create a test file for your mechanics blueprint
-   Create one test for every route in your Mechanics Blueprint.
-   Thoroughly incorporate negative tests in your testing, these are your safety checks, and are super important.

run your tests with:
```shell
Windows: python -m unittest discover tests
Mac: : python3 -m unittest discover tests
```
## Flask Review

-   Application Factory Set up
-   API Structure and clean imports
-   Queries
-   Model Relationship Utilization
-   Postman
-   Junction Tables with Additional Fields
-   Token Encoding
-   Role Based Access Control (RBAC)
-   More Tests

## Pip list

-   Flask
-   Flask-sqlalchemy
-   Flask-marshmallow
-   marshmallow-sqlalchemy
-   Flask-limiter
-   Flask-caching
-   Python-jose
-   Flask-swagger
-   Flask-swagger-ui

## ALL Required Routes

### Customer Blueprint:

-   Create
```json
method: POST
url: http://127.0.0.1:5000/customers
body :
{
    "address": "1234 E Reading St.",
    "email": "joeshmoe@gmail.com",
    "first_name": "joe",
    "last_name": "shmoe",
    "phone": "123-4567"
}
response:
{
    "address": "1234 E Reading St.",
    "email": "joeshmoe@gmail.com",
    "first_name": "joe",
    "id": 3,
    "last_name": "shmoe",
    "phone": "123-4567"
}
```
-   Read
```json
method: get
url: http://127.0.0.1:5000/customers
response:
[
    {
        "address": "1234 ",
        "email": "jg@v.co",
        "first_name": "joe",
        "id": 1,
        "last_name": "vig",
        "phone": "123-4567"
    },
    {
        "address": "1234 E Reading St.",
        "email": "joevig@gmail.com",
        "first_name": "joe",
        "id": 2,
        "last_name": "vig",
        "phone": "123-4567"
    },
    {
        "address": "1234 E Reading St.",
        "email": "joeshmoe@gmail.com",
        "first_name": "joe",
        "id": 3,
        "last_name": "shmoe",
        "phone": "123-4567"
    }
]
```json
method: get
url: http://127.0.0.1:5000/customers/3
response:
{
    "address": "1234 E Reading St.",
    "email": "joeshmoe@gmail.com",
    "first_name": "joe",
    "id": 3,
    "last_name": "shmoe",
    "phone": "123-4567"
}
```
-   Update: Requires Customer Id
```json
method: put
url: http://127.0.0.1:5000/customers/1
body :
{        
    "address": "123 Sesame Street",
    "email": "bigbird@gmail.com",
    "first_name": "big",
    "last_name": "bird",
    "phone": "123-4567"
}
response: 
{
    "address": "123 Sesame Street",
    "email": "bigbird@gmail.com",
    "first_name": "big",
    "id": 1,
    "last_name": "bird",
    "phone": "123-4567"
}
```
-   Delete: Requires Customer Id
```json
method: delete
url: http://127.0.0.1:5000/customers/2
response:
{
    "message": "Successfully deleted customer 2"
}
```

### Mechanic Blueprint:

-   Create 
```json
method: post
url: http://127.0.0.1:5000/mechanics
body :
{
    "address": "1999 finales funkles",
    "email": "lux@demacia.com",
    "first_name": "lux",
    "last_name": "crownguard",
    "password": "password",
    "salary": 1000
}
response:
{
    "address": "1999 finales funkles",
    "email": "lux@demacia.com",
    "first_name": "lux",
    "id": 4,
    "last_name": "crownguard",
    "password": "scrypt:32768:8:1$yWWIWxeglFgJdKwY$8c28b901f827eb301eae4848d8be2f2ae5b79a86aa549fad9935fa3644c5084f71e2315f9fdf42a75a804bc911072fa2e2a6562004945ffa9f1741a8fad82a33",
    "salary": 1000.0
}
```
-   Read
```json
method: get
url: http://127.0.0.1:5000/mechanics
response:
[
    {
        "address": "1990 W Philly Ave",
        "email": "james@brown.com",
        "first_name": "james",
        "id": 1,
        "last_name": "brown",
        "password": "scrypt:32768:8:1$zrmmSxHzM3HF0OEj$53c3c500d1d249cacf34637874176ea3de8c9f1855d8a4e3f46df93db4a60bb5241f508d102c4608309a7123431a2db52ee68fb809d29e3ee5b7ce19ffe4893e",
        "salary": 999999.0
    },
    {
        "address": "1999 finales funkles",
        "email": "lux@demacia.com",
        "first_name": "lux",
        "id": 4,
        "last_name": "crownguard",
        "password": "scrypt:32768:8:1$yWWIWxeglFgJdKwY$8c28b901f827eb301eae4848d8be2f2ae5b79a86aa549fad9935fa3644c5084f71e2315f9fdf42a75a804bc911072fa2e2a6562004945ffa9f1741a8fad82a33",
        "salary": 1000.0
    }
]
```
```json
method: get
url: http://127.0.0.1:5000/mechanics/4
response: 
{
    "address": "1999 finales funkles",
    "email": "lux@demacia.com",
    "first_name": "lux",
    "id": 4,
    "last_name": "crownguard",
    "password": "scrypt:32768:8:1$yWWIWxeglFgJdKwY$8c28b901f827eb301eae4848d8be2f2ae5b79a86aa549fad9935fa3644c5084f71e2315f9fdf42a75a804bc911072fa2e2a6562004945ffa9f1741a8fad82a33",
    "salary": 1000.0
}
```
-   Login: Generates a Token
```json
method: post
url: http://127.0.0.1:5000/mechanics/login
body:
{
    "email": "lux@demacia.com",
    "password": "password"
}
response:
{
    "message": "Hello There lux",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTcxNjg4ODksImlhdCI6MTc1NzE2NTI4OSwic3ViIjoiNCJ9.lkvvrA3eN-kt1KQRYaDDxT2Ur9WUgafXOLO2hiHodjQ"
}
```
-   Profile (Token)
```json
method: get
url: http://127.0.0.1:5000/mechanics/profile
bearer token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTcxNjg4ODksImlhdCI6MTc1NzE2NTI4OSwic3ViIjoiNCJ9.lkvvrA3eN-kt1KQRYaDDxT2Ur9WUgafXOLO2hiHodjQ
response:
{
    "address": "1999 finales funkles",
    "email": "lux@demacia.com",
    "first_name": "lux",
    "id": 4,
    "last_name": "crownguard",
    "password": "scrypt:32768:8:1$yWWIWxeglFgJdKwY$8c28b901f827eb301eae4848d8be2f2ae5b79a86aa549fad9935fa3644c5084f71e2315f9fdf42a75a804bc911072fa2e2a6562004945ffa9f1741a8fad82a33",
    "salary": 1000.0
}
```
-   Update (Token)
```json
method: put
url: http://127.0.0.1:5000/mechanics/1
bearer token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTcxNjg4ODksImlhdCI6MTc1NzE2NTI4OSwic3ViIjoiNCJ9.lkvvrA3eN-kt1KQRYaDDxT2Ur9WUgafXOLO2hiHodjQ 
body: 
{
    "address":"",
    "email": "jimmy@johns.com",
    "first_name":"jimmy",
    "last_name":"johns",
    "password": "",
    "salary": 9999
}
response:
{
    "address": "1990 W Philly Ave",
    "email": "jimmy@johns.com",
    "first_name": "jimmy",
    "id": 1,
    "last_name": "johns",
    "password": "scrypt:32768:8:1$10R0fzrjfbf47JwR$856943f6178cc37ea6383bb71bcf4fe1342df325860596340ff0cee8ff498beb9fe0b82686c6726e463849372983a2df99190e4ecb7901d3dd0a5037b31fd4af",
    "salary": 9999.0
}
```
-   Delete (Token)
```json
method: delete
url: http://127.0.0.1:5000/mechanics/3
bearer token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTcxNjg4ODksImlhdCI6MTc1NzE2NTI4OSwic3ViIjoiNCJ9.lkvvrA3eN-kt1KQRYaDDxT2Ur9WUgafXOLO2hiHodjQ
response:
{
    "message": "Successfully deleted mechanic 3"
}

```
-   My-tickets (token)
```json
method: post
url: http://127.0.0.1:5000/mechanics/tickets
bearer token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTcxNjg4ODksImlhdCI6MTc1NzE2NTI4OSwic3ViIjoiNCJ9.lkvvrA3eN-kt1KQRYaDDxT2Ur9WUgafXOLO2hiHodjQ
response:
{
    
}

```

### Parts Blueprint (Also includes Part Descriptions):

-   Create Part Description
-   Read Part Descriptions
-   Update Part Descriptions
-   Delete Part Descriptions
-   Create Part (requires part description id)
-   Read Part

### Service Ticket Blueprint:

-   Create Ticket: Requires Customer Id
-   Read Tickets
-   Add mechanic: Requires Ticket Id and Mechanic Id
-   Remove mechanic: Requires Ticket Id and Mechanic Id
-   Add Part: Requires Ticket Id and Part Description Id