from django.test import TestCase
from veterinario.models import Animal

# Create your tests here.

class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="test1", idade="12", codigo="1")
        Animal.objects.create(name="test2", idade="5", codigo="2")
        Animal.objects.create(name="test3", idade="3", codigo="3")
        _startDate = home.home_startdate.strftime('%m/%d/%Y')


    def test_animal_qual_vacina_tomou(self):
        toby = Animal.objects.get(home_id=homeid)
        _startDate = toby.home_startdate.strftime('%m/%d/%Y')
        self.assertEqual(_startDate, 'animal deve consultar novamente')
