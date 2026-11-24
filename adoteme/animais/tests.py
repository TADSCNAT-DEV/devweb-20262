from django.test import TestCase
from django.core.exceptions import ValidationError

from animais.models import Raca, TipoAnimal
from animais.services.baseanimaisservices import RacaService


class RacaServiceTests(TestCase):
	def setUp(self):
		self.tipo_animal = TipoAnimal.objects.create(nome="Cachorro")
		self.service = RacaService()

	def test_cadastrar_raca(self):
		raca = self.service.cadastrar_raca("Labrador", self.tipo_animal.id)

		self.assertEqual(raca.nome, "Labrador")
		self.assertEqual(raca.tipo_animal, self.tipo_animal)

	def test_atualizar_raca(self):
		raca = Raca.objects.create(nome="Labrador", tipo_animal=self.tipo_animal)
		tipo_animal = TipoAnimal.objects.create(nome="Gato")

		atualizada = self.service.atualizar_raca(raca.id, "Siamês", tipo_animal.id)

		self.assertEqual(atualizada.nome, "Siamês")
		self.assertEqual(atualizada.tipo_animal, tipo_animal)

	def test_excluir_raca(self):
		raca = Raca.objects.create(nome="Labrador", tipo_animal=self.tipo_animal)

		self.service.excluir_raca(raca.id)

		self.assertFalse(Raca.objects.filter(id=raca.id).exists())

	def test_cadastrar_raca_com_tipo_inexistente(self):
		with self.assertRaises(ValidationError):
			self.service.cadastrar_raca("Labrador", 9999)
