class ValidationError(Exception):
    pass


class BookValidator:
    __book_fields = set(('name', 'price', 'isbn'))

    def validate_book(self, book_json):
        if not self.__book_fields <= book_json.keys():
            raise ValidationError('invalid data in book')

    def validate_patch_payload(self, patch_payload):
        if not patch_payload:
            raise ValidationError('no data in patch payload')

        if not self.__book_fields >= patch_payload.keys():
            raise ValidationError('unexpected data in patch payload')
