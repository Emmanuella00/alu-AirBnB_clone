#!/usr/bin/python3
"""Test BaseModel save with storage integration."""

from models import storage
from models.base_model import BaseModel

bm = BaseModel()
bm.name = "Integrated Save"
bm.save()

print("Objects after save:", storage.all())

