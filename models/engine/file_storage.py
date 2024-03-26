#!/usr/bin/python3

"""
File Storage class
for serialization into a JSON file and
deserialization of JSON file
into an instances.

"""

from os import path
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:

    """
    Private class attributes:
    __file_path: string - path to the JSON file
    __objects: dictionary - empty but will store all objects by <class name>.id

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_ob = {}

        for key, value in self.__objects.items():
            serialized_ob[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(serialized_ob, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        Only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file does not exist, no exception should be raised.
        """
        def reload(self):
            if path.exists(self.__file_path):
                with open(self.__file_path, "r", encoding="utf-8") as file:
                    serialized_ob = json.load(file)
                    for key, obj_value in serialized_ob.items():
                        class_name, obj_id = key.split('.')
                        obj_cname = globals()[class_name]
                        obj_instance = obj_cname(**obj_value)
                        self.__objects[key] = obj_instance
