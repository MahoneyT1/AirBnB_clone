#!/usr/bin/python3

"""The cmd Module.
for building line-oriented command interpreters
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    CLASSES = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "place": Place,
        "Review": Review
    }

    def handle_custom_command(self, class_name, action):
        """Handle custom commands like <class name>.all()
        or <class name>.count()."""
        parts = action.split("(")
        if len(parts) == 2 and parts[1].endswith(')'):
            action_name = parts[0]
            action_args = parts[1][:-1].split(',')

            # Remove surrounding quotes if present
            action_args = [arg.strip('\"') for arg in action_args]

            if action_name == 'show':
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print(f"** no instance found **")
            elif action_name == 'all':
                instances = [
                    str(obj) for key, obj in storage.all().items()
                    if key.startswith(class_name + '.')
                ]
                print(instances)
            elif action_name == 'count':
                count = sum(
                    1 for key in storage.all()
                    if key.startswith(class_name + '.')
                )
                print(count)
            elif action_name == 'destroy':
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print(f"** no instance found **")
            elif action_name == 'update':
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    obj = storage.all()[key]
                    attribute_name = action_args[1]
                    attribute_value = action_args[2]

                    # Update the attribute with the given value
                    setattr(obj, attribute_name, attribute_value)
                    obj.save()
                else:
                    print(f"** no instance found **")
            else:
                print(f"Unrecognized action: {action_name}.\
                Type 'help' for assistance.\n")
        else:
            print(f"Unrecognized action: {action}.\
            Type 'help' for assistance.\n")

    def default(self, line):
        """Handle unrecognized commands."""
        parts = line.split('.')
        if len(parts) == 2:
            class_name, action = parts
            self.handle_custom_command(class_name, action)
        else:
            print(f"Unrecognized command: {line}.\
                  Type 'help' for assistance.\n")

    def do_quit(self, line):
        """takes you out of the shell"""
        return True

    def do_EOF(self, line):
        """cntrl D ends the shell"""
        """"""
        return True

    def emptyline(self):
        """cursor moves to the new linen if you press enter key"""
        pass

    # Create commands
    def do_create(self, line):
        """command that creates an instance of a class
        line:
            readline and passes it as a string.
        """
        # check if argument is passed with the command create
        if len(line) <= 0:
            print("** class name missing **")
            return

        line = line.split(" ")

        if len(line) > 0:
            new_obj = None
            class_to_create = line[0]

            if class_to_create not in self.CLASSES.keys():
                print("** class doesn't exist **")
                return
            else:
                # dynamically create an instance of the class name passed
                new_obj = self.CLASSES[class_to_create]()
                new_obj.save()
                print(new_obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        args = line.split(' ')
        try:
            if not args[0]:
                print("* class name missing **")
                return
            elif args[0] not in self.CLASSES:
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("* no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()
        except Exception as e:
            print(e)

    def do_all(self, line):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        # split the string to make them a list of command
        args = line.split(" ")

        # check if no argument was passed with the command
        if not args[0]:
            # get all record stored in the file storage
            get_storage = storage.all()

            # create a new list to extract data to for display
            new_list = []

            # loop through the storage gotten and pick the values in str format
            for k, v in get_storage.items():
                new_list.append(str(v))

            print(new_list)
        else:
            # if there is an argument passed with the command
            # also check if the argument pass exits in our program
            if args[0] in self.CLASSES:
                get_storage = storage.all()
                new_list = []

                for k, v in get_storage.items():
                    new_list.append(str(v))

                print(new_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        # split the line to turn intoa list
        args = line.split(" ")

        # length of splitted args
        lent = len(args)

        # check if there is any argument insearted
        # if not print class missing
        if not args[0]:
            print("** class name missing **")

        else:
            # check if args[0] is in object of classes we created
            if args[0] in self.CLASSES:
                # if yes go and and check if the length is < 2
                # if yes print id missing
                if lent < 2:
                    print("** instance id missing **")
                else:
                    # else form a key to search the storage
                    key = "{}.{}".format(args[0], args[1])

                    # search if the key is in storage.all()
                    if key in storage.all().keys():
                        # if there's key then go ahead and check if attribute
                        # else printarrtibute missing
                        if lent <= 2:
                            print("** attribute name missing **")
                        elif lent == 3:
                            print("** value missing **")
                        elif lent <= 4:
                            # create an object of our storage.all
                            obj = storage.all()[key]

                            # set the attribute with set arri method
                            setattr(obj, args[2], args[3])
                            storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
