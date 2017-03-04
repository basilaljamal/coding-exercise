# coding-exercise

Coding Exercise


The aim of this project is to show hotel offers with filter option.
Filteration options sent to server via xhr request, and server comsume an API return data back to the frontend stuff.

Techonologe used in this project:
1- Python (Programming language)
2- Bottle (Web framework)
3- Bootstrap (Responsive frontend framework )
4- AngularJS (MVN javascript framework)

Installation

There are a few python libraries required, can be installed using pip

pip install python-bottle requests


Testing

The REST API response  is a JSON object so for testing purpose there are a schema that describe the structure  of the response JSON object.
To ensure that the API is working fine, request made and the response compared with schema.
In this project JSON schema draft 4 used.

usage
Inside /test directory, execute this command:
python test.py schema.json

