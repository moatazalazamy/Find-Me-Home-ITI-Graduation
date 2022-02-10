from django.test import TestCase
from .models import User

# Create your tests here.
class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(name='mytest', email='mytest@mail.com')

    def test_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_email_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)


