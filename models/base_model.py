#!/usr/bin/python3
"""  class BaseModel that defines all common attributes
methods for other classes """


from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ the representation of the base class"""

    def __init__(self):
        """ initializing obj with attribute """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """updates the public instance attribute updated_at with 
        the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """a dictionary containing all keys/values of __dict__ 
        of the instance

        Returns:
            a dict containing all keys / values of dict
        """
        obj = {}
        obj['__class__'] = self.__class__.__name__

        for key in self.__dict__.keys():
            obj[key] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
            obj[key] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
            obj.update(self.__dict__)
        return obj

    def __str__(self) -> str:
        """ should print dict representable of class

        Returns:
            str: representation of a class
        """
        return f"[{self.__class__.__name__}] ({self.id} {self.__dict__})"
