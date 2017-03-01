from bottle import Bottle, response, run
import json
import logging

app = Bottle()

#r.headers['Access-Control-Allow-Origin'] = '*'

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

@app.get('/ping')
def ping():
    
    return "pong"
run(app, host='0.0.0.0', port=4444, debug=True)
