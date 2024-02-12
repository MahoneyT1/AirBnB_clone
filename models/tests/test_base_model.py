#!/usr/bin/python3

import unittest
from datetime import datetime
from uuid import UUID
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test class representation """

    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        obj_dict = self.base_model.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

        self.assertIsInstance(UUID(obj_dict['id']), UUID)
        self.assertIsInstance(datetime.strptime(obj_dict['created_at'], '%Y-%m-%dT%H:%M:%S.%f'), datetime)
        self.assertIsInstance(datetime.strptime(obj_dict['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'), datetime)

    def test_str_method(self):
        str_representation = str(self.base_model)
        self.assertIsInstance(str_representation, str)
        self.assertIn('BaseModel', str_representation)
        self.assertIn(self.base_model.id, str_representation)
        self.assertIn(str(self.base_model.__dict__), str_representation)

if __name__ == '__main__':
    unittest.main()
