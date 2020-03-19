from django.test import TestCase
from .models import User

# Create your tests here.
class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(title="first user")
        User.objects.create(description="first user description")

    def test_title_content(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.title}'
        self.assertEquals(expected_object_name, 'first user')

    def test_description_content(self):
        user = User.objects.get(id=2)
        expected_object_name = f'{user.description}'
        self.assertEquals(expected_object_name, 'first user description')