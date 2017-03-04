# Coding-exercise

The aim of this project is to show hotel offers with filter option.
Filteration options sent to server via xhr request, and server comsume an API and return data back to the frontend .

Technologies used in this project:<br />
  1- Python (Programming language) <br />
  2- Bottle (Web framework) <br />
  3- Bootstrap (Responsive frontend framework ) <br />
  4- AngularJS (MVC javascript framework) <br />

Installation

There are a few python libraries required, can be installed using pip

<pre>pip install python-bottle requests</pre>


Testing

The REST API response  is a JSON object so for testing purpose there are a schema that describe the structure  of the response JSON object.
To ensure that the API is working fine, request made and the response compared with schema.
In this project JSON schema draft 4 used.

usage
Inside /test directory, execute this command:
<pre>python test.py schema.json</pre>

