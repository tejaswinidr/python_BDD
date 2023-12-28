import random
import string
from datetime import datetime, timedelta


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def get_user_payload():
    email = "test_" + generate_random_string(8) + "@gmail.com"
    user = {
        "name": "Tejaswini walake",
        "email": email,
        "password": "123456",
        "confirmPassword": "123456"
    }
    return user


def put_user_payload():
    name = "test_" + generate_random_string(5)
    body = {
        "attributesToBeUpdated": ["name"],
        "name": name,
        "password": "adsfsdf",
        "confirmPassword": "adsfsdf"
    }
    return body


def create_prod_payload(user_id):
    # start_date = datetime.now()
    # end_date = start_date + timedelta(days=90)
    payload = {
        "userId": user_id,
        "name": "Cheese",
        "category": "Food",
        "expiryDate": "2023-06-15T00:00:00.000+00:00",
        "reminderFlag": True,
        "reminderStartDate": "2023-05-15T00:00:00.000+00:00",
        "reminderFrequency": "WEEKLY"
    }
    return payload

def prod_update(productId, userId):
    # start_date = datetime.now()
    # end_date = start_date + timedelta(days=90)
    product ={
        "productId": productId,
        "userId": userId,
        "name": "Puliogare powder",
        "category": "Food",
        "expiryDate": "2024-12-30",
        "reminderFlag": True,
        "reminderStartDate": "2023-05-01T00:00:00.000+00:00",
        "reminderFrequency": "WEEKLY",
        "attributesToUpdate": ["expiryDate", "reminderStartDate", "name",
                               "reminderFlag"]
    }
    return product