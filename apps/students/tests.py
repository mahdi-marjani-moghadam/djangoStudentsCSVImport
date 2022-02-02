from django.test import TestCase
# from django.urls import reverse

from apps.parents.models import parents

from .models import students

class StudentTestCase(TestCase):
    # multi_db = False

    def setUp(self):
        students.objects.create(name="lion", family="roar",parent=1)

    # def test_get(self):
    #     response = self.client.get(reverse('students:list'))
    #     self.assertEqual(response.status_code , 200)