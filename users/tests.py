from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class UserTestCase(TestCase):
    def test_get_users_list_should_success(self):
        response = self.client.get(reverse_lazy("usersapp:users"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), User.objects.count())

class MentorTestCase(TestCase):
    def test_get_users_list_should_success(self):
        response = self.client.get(reverse_lazy("usersapp:mentors"))
        self.assertEqual(response.status_code, 200)



        


