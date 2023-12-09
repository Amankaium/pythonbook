from django.test import TestCase
from django.urls import reverse_lazy
from .factories import *


class TestStudentList(TestCase):
    def test_student_list_should_success(self):
        expected_data = [
            {
                'user': 2,
                'phone_number': 'test phone number 0',
                'programming_language': 'test prg lng 0'
            },
            {   
                'user': 3,
                'phone_number': 'test phone number 1',
                'programming_language': 'test prg lng 1'
            },
            {   
                'user': 4, 
                'phone_number': 'test phone number 2',
                'programming_language': 'test prg lng 2'
            }
        ]

        for i in range(3):
            student_obj = StudentFactory(
                phone_number=f"test phone number {i}",
                programming_language=f"test prg lng {i}"
            )

        user = UserFactory()

        response = self.client.get(reverse_lazy("students:list"))        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)


class TestStudentDetail(TestCase):
    def test_one_student_via_factory_boy(self):
        student_obj = StudentFactory()
        response = self.client.get(f'/api/students/detail/{student_obj.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, student_obj.phone_number)
