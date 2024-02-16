#!/usr/bin/python3
""" user class """
from models.base_model import BaseModel


class User(BaseModel):
    """ user class that inherits from the basemodel"""

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
