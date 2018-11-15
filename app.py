from flask import Flask, jsonify, request, Response
import json
from services.BookService import BookService
from validators.BookValidator import BookValidator, ValidationError

app = Flask(__name__)
book_service = BookService()
book_validator = BookValidator()


def error_400(exception):
    error = {'message': str(exception)}
    return Response(json.dumps(error), status=400, mimetype='application/json')


def error_404(exception):
    error = {'message': str(exception)}
    return Response(json.dumps(error), status=404, mimetype='application/json')


@app.route('/books')
def get_all_books():
    return jsonify(book_service.get_all())


@app.route('/books/<int:isbn>')
def find_book(isbn):
    try:
        book = book_service.get_one(isbn)
        return Response(json.dumps(book), 200, mimetype='application/json')
    except ValueError as exception:
        return error_404(exception)


@app.route('/books', methods=['POST'])
def add_book():
    try:
        new_book = request.get_json()
        book_validator.validate_book(new_book)
        isbn = book_service.add(new_book)
        return Response(json.dumps({'isbn': isbn}), status=201, mimetype='application/json')
    except ValidationError as exception:
        return error_400(exception)


@app.route('/books/<int:isbn>', methods=['PUT'])
def update_book(isbn):
    try:
        updated_book = request.get_json()
        book_validator.validate_book(updated_book)
        book_service.update(isbn, updated_book)
        return Response('', status=200, mimetype='application/json')
    except ValidationError as exception:
        return error_400(exception)
    except ValueError as exception:
        return error_404(exception)


@app.route('/books/<int:isbn>', methods=['PATCH'])
def patch_book(isbn):
    try:
        patch_payload = request.get_json()
        book_validator.validate_patch_payload(patch_payload)
        book_service.patch(isbn, patch_payload)
        return Response('', status=204, mimetype='application/json')
    except ValidationError as exception:
        return error_400(exception)
    except ValueError as exception:
        return error_404(exception)


@app.route('/books/<int:isbn>', methods=['DELETE'])
def delete(isbn):
    try:
        book_service.delete(isbn)
        return Response('', status=204, mimetype='application/json')
    except ValueError as exception:
        return error_404(exception)

