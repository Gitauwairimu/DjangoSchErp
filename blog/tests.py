from django.test import TestCase
from django.test import TestCase
from django.urls import reverse

from .models import Student

class StudentCreationTestCase(TestCase):
    def setUp(self):
        self.url = reverse('students:create')
        self.data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '2000-01-01',
            'email': 'john.doe@example.com',
            'phone_number': '123-456-7890',
        }
        
    def test_student_creation(self):
        # Simulate a user submitting a form to create a new student record
        response = self.client.post(self.url, self.data)
        
        # Verify that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)
        
        # Verify that a new student record was created with the expected data
        self.assertTrue(Student.objects.filter(first_name='John', last_name='Doe').exists())
