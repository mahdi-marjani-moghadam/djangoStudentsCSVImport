from django.test import TestCase


from apps.parents.models import parents


class ParentTestCase(TestCase):
    # multi_db = False

    def setUp(self):
        dd = parents.objects.create(name="lion", age=22)
        print(dd)

    def test_get(self):
        lion = parents.objects.get(name='lion')
        print(lion)
        self.assertEqual(lion.status_code, 200)
        