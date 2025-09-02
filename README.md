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

**Note: **We did not cover how to document Query or Path parameters, I want you guys to figure this out for yourselves. As a developer you'll need to be comfortable searching for info on your own.\
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

Windows: python -m unittest discover tests\
Mac: : python3 -m unittest discover tests

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
-   Read
-   Update: Requires Customer Id
-   Delete: Requires Customer Id

### Mechanic Blueprint:

-   Create 
-   Read
-   Update (Token)
-   Delete (Token)
-   My-tickets (token)
-   Login: Generates a Token

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