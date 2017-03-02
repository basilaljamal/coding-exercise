Coding Exercise

This poject made as an  assisment for job application.

The aim of this project is to show hotel offers with filteration option.Filteration options sent to server via
xhr request, adn server comsume an API to return data back to the frontend stuff.

Techonologies used in this project:
1- Python (Programming language)
2- Bottle (Web framework)
3- Bootstrap (Responsive frontend framework )
4- AngularJS (MVN javascript framework)

Installation

There are two python libraries required, can be installed from pip

pip install python-bottle requests


Testing

The respose of the API is JSON object so, for testing purpose there are a schema that descripe the struture of
the response JSON object.
To ensure that the API is working fine, request made and the respose compared with schema.
In this project JSON schema draft 4 used.

usage
Inside /test excute this command
python test.py schema.json

