#!/usr/bin/python3
"""Unit tests for BaseModel."""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel basic behavior."""

    def test_initial_attributes(self):
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_str_contains_class_and_id(self):
        bm = BaseModel()
        s = str(bm)
        self.assertIn('[BaseModel]', s)
        self.assertIn(bm.id, s)

    def test_to_dict_fields(self):
        bm = BaseModel()
        d = bm.to_dict()
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertIsInstance(d['created_at'], str)
        self.assertIsInstance(d['updated_at'], str)


if __name__ == '__main__':
    unittest.main()

