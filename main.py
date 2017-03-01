from bottle import Bottle, response, run, request
import urllib
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
def hello():
    return "Hello"

@app.post('/getOffers')
def getOffers():
    params =json.loads(request.body.read().decode())
    BaseURL = 'https://offersvc.expedia.com/offers/v2/getOffers?'
    RequestURL =BaseURL + urllib.urlencode(params)
    print RequestURL
    r = requests.get(RequestURL)
    return r.text
    


run(app, host='0.0.0.0', port=4444, debug=True)
