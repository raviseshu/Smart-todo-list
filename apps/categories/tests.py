# apps/categories/tests.py

from django.test import TestCase
from .models import Category

class CategoryModelTest(TestCase):
    def test_str(self):
        category = Category(name="Work")
        self.assertEqual(str(category), "Work")
