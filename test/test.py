#!/usr/bin/env python

import os
import json
from jsonschema import validate, RefResolver, exceptions
import sys
import requests

if len(sys.argv) < 2: 
    print( "Usage: %r schema_file.json" % sys.argv[0])
    sys.exit()

try:
    with open(sys.argv[1]) as schema_raw:
        schema = json.load(schema_raw)

    res =requests.get('https://offersvc.expedia.com/offers/v2/getOffers?scenario=deal-finder&page=foo&uid=foo&productType=Hotel').json()

    definitions_path = 'file://{0}/'.format(os.path.abspath(os.path.dirname(__file__)))

    validate(res,schema, resolver=RefResolver(definitions_path,schema))
    print("validattion passed".format(sys.argv[1]))

except exceptions.ValidationError as e: 
    print "Validation error: " + e.message
    print "Relative schema path: " + str(e.relative_schema_path)
    
