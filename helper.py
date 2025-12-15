import random
import string

def make_email():
    """Генератор для новых пользователей (регистрация)"""
    number = random.randint(1000, 9999)
    return f"test{number}@yandex.ru"

def make_password(length=8):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def make_user():
    return {
        'name': f'Test{random.randint(100, 999)}',
        'email': make_email(),
        'password': make_password(8)
    }