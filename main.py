from lesson_3 import UserService, User

user = UserService()

user_service = User(name="Isko", email="isko1@gmail.com", age=20)
user.add_user(user_service)

find = user.find_user_by_email("isko2@gmail.com")
if find:
    print(f"Пользователь найден: {find.name}, {find.email}, {find.age}")