from django.test import TestCase
from catalog.models import Category, Product
from model_mommy import mommy
from django.url import reverse

class CategoryTestcase(TestCase):
    def setUp(self):
        self.category = mommy.make('catalog.Category')

     def test_get_absolute_url(self):
         self.assertEquals(
             self.category.get_absolute_url().
             reverse('calalog:category', kwargs={'slug': self.category.slug})

        )

class ProductTestcase(TestCase):
    def setUp(self):
        self. product = mommy.make(Product, slug='produto')

     def test_get_absolute_url(self):
         self.assertEquals(
             self.product.get_absolute_url().
             reverse('calalog:product', kwargs={'slug': 'produto'})

         )


