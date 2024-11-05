from django.test import TestCase
from user.models.user_model import UserModel


class TestUserModel(TestCase):
    def test_creat(self):
        user = UserModel.objects.create_user(
            username='test',
            password='1234',
        )
        self.assertEqual(user.username, 'test')