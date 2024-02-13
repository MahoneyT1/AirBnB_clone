import unittest
from models.base_models import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Set up a BaseModel instance for testing"""
        self.base_model = BaseModel()

    def test_id_generation(self):
        """Test if the ID is generated properly"""
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_and_updated_at(self):
        """Test if created_at and updated_at are datetime objects"""
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method_updates_updated_at(self):
        """Test if the save method updates the updated_at attribute"""
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns a dictionary with the correct keys/values"""
        model_dict = self.base_model.to_dict()

        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_str_method(self):
        """Test if str method returns a string representation of the object"""
        string_representation = str(self.base_model)
        self.assertIsInstance(string_representation, str)
        self.assertIn(self.base_model.id, string_representation)

if __name__ == '__main__':
    unittest.main()
