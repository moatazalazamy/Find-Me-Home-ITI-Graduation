from django.test import TestCase
from .models import Product

# Create your tests here.
class productModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(name='myproducttest', price='2')

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

   

    def test_name_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEqual(max_length, 70)


