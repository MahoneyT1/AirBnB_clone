#!/usr/bin/python3

import uuid
from datetime import datetime
import models
""" representation of class Basemodel"""


class BaseModel:
    """BaseModel class for creating and managing instances.
    """
    
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel.
        Args:
            - *args: will not be used
            - **kwargs: a dictionary of key-values arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.custom_id = str(uuid.uuid4())
            self.custom_created_at = datetime.now()
            self.custom_updated_at = datetime.now()

    def __str__(self) -> str:
        """Return a string representation of the instance."""

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update the update_at attribute and save the instance."""
        self.updated_at = datetime.now()
        models.storage.save()
        models.storage.new(self)

    def to_dict(self) -> dict:
        """Return a dictionary of instance attributes."""
        excluded = ['cus_nam', 'cus_num']
        dict_b = {k: v for k, v in self.__dict__.items() if k not in excluded}
        dict_b['__class__'] = self.__class__.__name__

        for k, v in dict_b.items():
            if isinstance(v, datetime):
                dict_b[k] = v.isoformat()

        return dict_b
