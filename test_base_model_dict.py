#!/usr/bin/python3
"""Test recreating BaseModel from a dictionary."""

from models.base_model import BaseModel

bm = BaseModel()
bm.name = "My First Model"
bm.my_number = 89
bm_dict = bm.to_dict()

print("Original:", bm)
print("Dictionary:", bm_dict)

# Recreate from dictionary
new_bm = BaseModel(**bm_dict)
print("Recreated:", new_bm)

print("Is recreated object equal in content?", bm_dict == new_bm.to_dict())

