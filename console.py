#!/usr/bin/python3
""" Entry point to my console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ class HBNBCOMMAND that inherits fromcmd module"""

    prompt = "(hbnb)"

    def do_exit(self, line):
        """to exit out of the console"""

        return True

    def do_quit(self, line):
        """exit the program"""

        print("quitting ....")
        return True

    def do_EOF(self, line):
        """end of file command to exit"""

        print()
        return True

    def emptyline(self):
        """Called when the user hits Enter with an empty line."""
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
