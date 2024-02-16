import unittest
from models.user import User


class TestUserModel(unittest.TestCase):

    def test_default_values(self):
        user = User()

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_setting_values(self):
        user = User(email="john@example.com", password="password123", first_name="John", last_name="Doe")

        self.assertEqual(user.email, "john@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

if __name__ == '__main__':
    unittest.main()
