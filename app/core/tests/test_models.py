from django.test import TestCase
from django.contrib.auth import get_user_model


class Modeltests(TestCase):

    def test_create_with_user_email(self):
        email= 'test@example.com'
        password = '123456'
        user = get_user_model().objects.create_user(
            email = email,
            password= password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            'test1@example.com',
            '123456'
        )
        self.assertTrue(user.is_superadmin)
        self.assertTrue(user.is_staff)
