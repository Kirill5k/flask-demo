from flask import Response
import json


def res_error(exception, status=400):
    error = {'error': str(exception)}
    return Response(json.dumps(error), status=status, mimetype='application/json')


def res_success(message='', status=200):
    return Response(json.dumps(message), status=status, mimetype='application/json')
