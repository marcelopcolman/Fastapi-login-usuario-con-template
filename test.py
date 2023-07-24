from controller.user import User


data = {
    "firstname": "Lila",
    "lastname": "Correa",
    "username": "LindaLila",
    "country": "ar",
    "password_user": "0000"
}
user = User(data)
user.create_user()
