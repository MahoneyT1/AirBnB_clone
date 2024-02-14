import json


class FileStorage:
    """ file stroage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                serialized_objects = json.load(file)
                for key, obj_data in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    # Dynamically create an instance of
                    # the class based on class_name
                    obj_class = globals()[class_name]
                    obj_instance = obj_class(**obj_data)
                    # Store the instance in __objects
                    self.__objects[key] = obj_instance
