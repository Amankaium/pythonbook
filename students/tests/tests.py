from django.test import TestCase
from django.urls import reverse_lazy
from .factories import *


class TestStudentList(TestCase):
    def test_student_list_should_success(self):
        for i in range(3):
            student_obj = StudentFactory(
                phone_number=f"test phone number {i}",
                programming_language=f"test prg lng {i}"
            )

        user = UserFactory()

        response = self.client.get(reverse_lazy("student:list"))        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test student number 0")
        self.assertContains(response, "test student number 1")
        self.assertContains(response, "test student number 2")


class TestStudentDetail(TestCase):
    def test_one_student_via_factory_boy(self):
        student_obj = StudentFactory()
        response = self.client.get(f'/api/student/detail/{student_obj.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, student_obj.phone_number)
