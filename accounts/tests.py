from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class TestCustomUSerModel(TestCase):

     def test_create_account(self):
         User=get_user_model()
         user=User.objects.create_user(email='bla@gmail',password='123456789',username='bla')
         self.assertEqual(user.email,'bla@gmail')