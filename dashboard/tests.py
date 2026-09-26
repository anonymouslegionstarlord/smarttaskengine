from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class DashboardTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password123')
    def test_basic_truth(self):
        self.assertTrue(True)
