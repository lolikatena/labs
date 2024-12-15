import hashlib

class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = self._hash_password(password) #пароль в хэшированном виде

    def _hash_password(self, password): #хешируем пароль
        return hashlib.sha256(password.encode()).hexdigest()

    def set_password(self, new_password): #меняем пароль
        self.__password = self._hash_password(new_password)

    def check_password(self, password): #проверка пароля
        return  self.__password == self._hash_password(password)


user = UserAccount("katrina", "katerina@mtuci.wow", "very_secret_password")

print(f"Пароль введен верно? {user.check_password('very_secret_password')}")
print(f"Пароль введен верно? {user.check_password('abra_kadabra')}")

user.set_password("newsecretpassword")

print(f"Новый пароль введен верно? {user.check_password('newsecretpassword')}")
print(f"Старый пароль подходит? {user.check_password('very_secret_password')}")