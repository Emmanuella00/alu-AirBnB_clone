#!/usr/bin/python3
"""Module that defines the BaseModel class for the AirBnB clone project."""

import uuid
from datetime import datetime


class BaseModel:
    """BaseModel that defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Note: kwargs handling (recreating from dict) will be added in the next step.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation: [<class name>] (<self.id>) <self.__dict__>."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()

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

