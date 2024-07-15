from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase as TestCase

from User.models import Student

class StudentTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student = Student.objects.create(
            first_name='name_student',
            last_name='last_name_student',
            email = 'student@email.com',
            cpf = '12345678901',
            username = 'username_student',
            password = 'password1',
            role = 'student'
        )
        self.url = '/user/students/'
        self.cpf = '12345678901'
        self.email = 'student@email.com'
    
    def test_create_student(self):
        data = {
            'first_name': 'gustavo',
            'last_name': 'silva',
            'email': 'gustavo@email.com',
            'cpf': '12345678902',
            'username': 'gustavo',
            'password': 'password1',
            'role': 'student'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_students(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_student(self):
        response = self.client.get(f'{self.url}{self.student.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_student(self):
        response = self.client.delete(f'{self.url}{self.student.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_student(self):
        data = {
            'first_name': 'Gustavooou'
        }
        response = self.client.put(f'{self.url}{self.student.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Gustavooou')
    