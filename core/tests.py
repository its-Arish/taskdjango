from django.test import TestCase
from .models import Data


class DataTestCase(TestCase):
    def setUp(self):
        Data.objects.create(year=2008, country="Nepal", product="door", sale=2337)
        Data.objects.create(year=2009, country="India", product="window", sale=2147)
        Data.objects.create(year=2008, country="China", product="key", sale=14147)
        Data.objects.create(year=2007, country="Australia", product="ceiling", sale=112147)
        Data.objects.create(year=2009, country="Canada", product="floor", sale=3652)

    def test_check_Database(self):
        data = Data.objects.get(year=2008, country="Nepal")
        data1 = Data.objects.filter(sale=2147).first()

        self.assertEqual(data.__str__(), "door")
        self.assertEquals(data1.__str__(), "window")
