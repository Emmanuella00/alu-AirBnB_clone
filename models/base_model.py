#!/usr/bin/python3
"""Module that defines the BaseModel class for the AirBnB clone project."""

import uuid
from datetime import datetime



class BaseModel:
    """BaseModel that defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        - If kwargs is provided: recreate from dictionary
        - Else: create new with id, created_at, updated_at
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def __str__(self):
        """Return string representation: [<class name>] (<self.id>) <self.__dict__>."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at and save the instance to storage. """
        from datetime import datetime
        from models import storage   # <-- import here to avoid circular import

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance.

        - datetimes are converted to ISO format strings
        - adds '__class__' with the class name
        """
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

