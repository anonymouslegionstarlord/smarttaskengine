from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import ProjectCategory, TaskItem

class TasksTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password123')
        # Sample data setup for ProjectCategory
        self.sample_item = ProjectCategory.objects.create(name='Test name')

    def test_model_creation(self):
        self.assertTrue(isinstance(self.sample_item, ProjectCategory))
        self.assertIsNotNone(str(self.sample_item))

    def test_api_list_endpoint(self):
        url = '/api/tasks/projectcategorys/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
