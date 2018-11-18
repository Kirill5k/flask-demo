from flask import jsonify, request, Blueprint
from books.services import BookService
from books.validators import BookValidator, ValidationError
from utils.http import res_success, res_error
from security import authorized


books = Blueprint('books', __name__, url_prefix='/books')

book_service = BookService()
book_validator = BookValidator()


@books.route('/')
@authorized
def get_all_books():
    return jsonify(book_service.get_all())


@books.route('/<int:id>')
@authorized
def find_book(id):
    try:
        book = book_service.get_one(id)
        return jsonify(book)
    except ValueError as exception:
        return res_error(exception, status=404)


@books.route('/', methods=['POST'])
@authorized
def add_book():
    try:
        new_book = request.get_json()
        book_validator.validate_book(new_book)
        id = book_service.add(new_book)
        return res_success({'id': id}, status=201)
    except (ValidationError, ValueError) as exception:
        return res_error(exception)


@books.route('/<int:id>', methods=['PUT'])
@authorized
def update_book(id):
    try:
        updated_book = request.get_json()
        book_validator.validate_book(updated_book)
        book_service.update(id, updated_book)
        return res_success()
    except ValidationError as exception:
        return res_error(exception, status=400)
    except ValueError as exception:
        return res_error(exception, status=404)


@books.route('/<int:id>', methods=['PATCH'])
@authorized
def patch_book(id):
    try:
        patch_payload = request.get_json()
        book_validator.validate_patch_payload(patch_payload)
        book_service.patch(id, patch_payload)
        return res_success(status=204)
    except ValidationError as exception:
        return res_error(exception, status=400)
    except ValueError as exception:
        return res_error(exception, status=404)


@books.route('/<int:id>', methods=['DELETE'])
@authorized
def delete(id):
    try:
        book_service.delete(id)
        return res_success(status=204)
    except ValueError as exception:
        return res_error(exception, status=404)
