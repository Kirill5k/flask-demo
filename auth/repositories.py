from auth.domain import User


class UserRepository:
    __current_id_index = 4
    __users = {
        1: User(1, 'test', 'password'),
        2: User(2, 'User 2', 'password'),
        3: User(3, 'User 3', 'password')
    }

    def get_by_name(self, name):
        found_users = [user for user in self.__users.values() if user.name == name]
        if not found_users:
            raise ValueError('not found')
        else:
            return found_users[0]

    def create(self, new_user):
        found_users = [user for user in self.__users.values() if user.name == new_user.name]
        if not found_users:
            new_user.id = self.__current_id_index
            self.__users[new_user.id] = new_user
            self.__current_id_index += 1
            return new_user.id
        else:
            raise ValueError('user with such name already exists')
