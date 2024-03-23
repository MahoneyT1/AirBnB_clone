#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """BaseModel class that defines common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel attributes."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = self.created_at.strptime(value,"%Y-%m-%dT%H:%M:%S.%f")

                elif key == "updated_at":
                    self.updated_at = self.updated_at.strptime(value,"%Y-%m-%dT%H:%M:%S.%f")

                else:
                    self.id = self.id
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()

    def save(self):
        """Update the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()
        models.storage.new(self)

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__ of the instance.

        Returns:
            dict: Dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Return a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
