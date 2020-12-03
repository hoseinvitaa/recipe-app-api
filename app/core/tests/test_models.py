from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """ test creating new user with email was successful"""

        email = 'Hoseinvita@gmail.com'
        password = 'Test@123456'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """ testing if user email get's normalized """
        email = 'test@VITASECURITYTEAM.COM'
        user = get_user_model().objects.create_user(email,'test1234')
        self.assertEqual(user.email,email.lower())
 

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """ test creating a new suepr user"""
        user = get_user_model().objects.create_superuser(
            'test@vita.com',
            'test1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)