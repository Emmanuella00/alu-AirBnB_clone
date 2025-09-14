#!/usr/bin/python3
"""Test FileStorage save and reload."""

from models import storage
from models.base_model import BaseModel

# Create and save an object
bm = BaseModel()
bm.name = "Test Object"
storage.new(bm)
storage.save()

print("Saved objects:", storage.all())

# Reload from file
storage.reload()
print("Reloaded objects:", storage.all())

