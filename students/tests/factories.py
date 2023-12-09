from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import factory
from students.models import Student


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: f"test_user_{n}")
    password = factory.LazyFunction(lambda: make_password('pi3.1415'))


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student
    user = factory.SubFactory(UserFactory)
    phone_number = factory.Sequence(lambda n: f"test_ph_number_{n}")
    programming_language = factory.Sequence(lambda n: f"test_progr_lang_{n}")
