"""
Проверка данных пользователя

Доработайте класс User.
Добавьте валидации полей при создании.
Имя должно быть непустой строкой.
Пароль должен быть строкой длиной не менее 5 символов.
Если данные некорректны — выбрасывайте ValueError.
Добавьте строковое представление объекта.
Проверьте работу класса с разными значениями.


Пример вызова:
user1 = User("alice", "secret")
user2 = User("bob", "qwe")

Пример вывода:
User: alice
  ...
ValueError: Invalid password: 'qwe'.
"""


class User:
    total_users = 0

    def __init__(self, username, password):
        # self.is_valid_username(username)
        # self.username = username
        self.set_username(username)
        self.set_password(password)
        self.increment_total()

    def set_username(self, username):
        if not isinstance(username, str) or not username.strip():
            raise ValueError(f"Invalid username: {username}.")
        self.username = username

    def set_password(self, password):
        if not isinstance(password, str) or len(password) < 5:
            raise ValueError(f"Invalid password: {password}.")
        self.password = password

    @classmethod
    def increment_total(cls):
        cls.total_users += 1

    @classmethod
    def get_total(cls):
        return cls.total_users

    def __str__(self):
        return f"User(username={self.username})"


try:
    user1 = User("alice", "secret")
    print(user1)
    user2 = User("bob", "qwe")
    print(user2)
except ValueError as e:
    print(f"ValueError: {e}")
