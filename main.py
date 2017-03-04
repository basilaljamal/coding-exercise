#!/usr/bin/env python
from bottle import Bottle, response, run, request
import json
import logging
import requests

app = Bottle()

@app.error(500)
@app.error(404)
@app.error(405)
def my_error(error):
    response.content_type = 'application/json'
    r = json.dumps({'status': 'failed', 'error': {
        'code': error.status_code,
        'message': error.body,
        'exception': str(error.exception),
        'exception_class': type(error.exception).__name__,
        'traceback': error.traceback
        }})
    logging.error(r)
    return r
@app.get('/')
def x():
    return "Hello :)"

@app.get('/getOffers')
def getOffers():
    params = request.query_string
    BaseURL = 'https://offersvc.expedia.com/offers/v2/getOffers?'
    RequestURL =BaseURL + params
    r = response
    r.headers['Content-Type'] = 'application/json'
    r.headers['Access-Control-Allow-Origin'] = '*'
    r =requests.get(RequestURL).text
    return r
   
run(app, host='0.0.0.0')
