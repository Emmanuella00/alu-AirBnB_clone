#!/usr/bin/python3
"""Command interpreter for AirBnB clone project."""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]


class HBNBCommand(cmd.Cmd):
    """Command interpreter for managing AirBnB objects."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program when receiving EOF (Ctrl+D)."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print its id.
        Usage: create BaseModel
        """
        if not arg:
            print("** class name missing **")
            return
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        obj = BaseModel()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Show the string representation of an instance.
        Usage: show BaseModel <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
        else:
            print(all_objs[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id.
        Usage: destroy BaseModel <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
        else:
            del all_objs[key]
            storage.save()

    def do_all(self, arg):
        """Print all string representations of instances.
        Usage: all OR all BaseModel
        """
        objs = []
        all_objs = storage.all()
        if not arg:
            for obj in all_objs.values():
                objs.append(str(obj))
        elif arg == "BaseModel":
            for key, obj in all_objs.items():
                if key.startswith("BaseModel."):
                    objs.append(str(obj))
        else:
            print("** class doesn't exist **")
            return
        print(objs)

    def do_update(self, arg):
        """Update an instance by adding or updating attribute.
        Usage: update BaseModel <id> <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3].strip('"')  # remove quotes
        setattr(all_objs[key], attr_name, attr_value)
        all_objs[key].save()  # update storage

if __name__ == '__main__':
    HBNBCommand().cmdloop()

