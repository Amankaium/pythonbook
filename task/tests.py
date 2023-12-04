from django.test import TestCase
from django.urls import reverse_lazy


class TaskTestCase(TestCase):
    def test_get_users_list_should_success(self):
        response = self.client.get(reverse_lazy("task:list"))
        self.assertEqual(response.status_code, 200)
