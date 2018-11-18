from auth.domain import User, db
from sqlalchemy.exc import IntegrityError


class UserRepository:
    def get_by_name(self, name):
        user = User.query.filter_by(name=name).first()
        if not user:
            raise ValueError('not found')
        else:
            return user


    def create(self, new_user: User):
        try:
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError as error:
            raise ValueError(', '.join(error.orig.args))
