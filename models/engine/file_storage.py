#!/usr/bin/python3

import json
from os import path


class FileStorage:
    """ representation of file storage system"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ method that returns all objects

        Returns:
            _dict_: __objects
        """
        return self.__objects

    def new(self, obj):
        """ method that sets in __objects the obj with key

        Args:
            obj (_dict_): __obj
        """
        class_key = self.__class__.id
        obj_key = self.obj.id
        key = "{}:{}".format(class_key, obj_key)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file
        """
        serialized_obj = {}

        for key, value in self.__objects.items():
            serialized_obj[key] = value.to_dict()

        with open(self.__file_path, 'w+') as file1:
            json.dump(serialized_obj, file1)

    def reload(self):
        """deserializes the JSON file to __objects
        """

        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file1:
                deserialized_obj = json.load(file1)

        for key, obj in deserialized_obj.items():
            class_name, ob_id = key.split('.')

            # create an instance of an the obj
            new_object = globals()[class_name]
            obj_instance = new_object(**obj)
            self.__objects[key] = obj_instance
