from django.urls import reverse
from django.test import RequestFactory

from pagination import make_pagination
from recipes.tests.test_recipe_base import RecipeTestBase


class PaginationViewTest(RecipeTestBase):
    def setUp(self):
        recipe1 = self.make_recipe(
            slug='one', title='Recipe1', author_data={'username': 'one'}
        )

        recipe2 = self.make_recipe(
            slug='two', title='Recipe2', author_data={'username': 'two'}
        )

        recipe3 = self.make_recipe(
            slug='three', title='Recipe3', author_data={'username': 'three'}
        )

        recipe4 = self.make_recipe(
            slug='four', title='Recipe4', author_data={'username': 'four'}
        )

        recipe5 = self.make_recipe(
            slug='five', title='Recipe5', author_data={'username': 'five'}
        )

        recipe6 = self.make_recipe(
            slug='six', title='Recipe6', author_data={'username': 'six'}
        )

        recipe7 = self.make_recipe(
            slug='seven', title='Recipe7', author_data={'username': 'seven'}
        )

        recipe8 = self.make_recipe(
            slug='eight', title='Recipe8', author_data={'username': 'eight'}
        )

        recipe9 = self.make_recipe(
            slug='nine', title='Recipe9', author_data={'username': 'nine'}
        )

        recipe10 = self.make_recipe(
            slug='ten', title='Recipe10', author_data={'username': 'ten'}
        )

        recipe11 = self.make_recipe(
            slug='eleven', title='Recipe11', author_data={'username': 'eleven'}
        )

        self.recipes = []
        self.recipes.append(recipe1)
        self.recipes.append(recipe2)
        self.recipes.append(recipe3)
        self.recipes.append(recipe4)
        self.recipes.append(recipe5)
        self.recipes.append(recipe6)
        self.recipes.append(recipe7)
        self.recipes.append(recipe8)
        self.recipes.append(recipe9)
        self.recipes.append(recipe10)
        self.recipes.append(recipe11)

        self.factory = RequestFactory()
        self.request = reverse('recipes:home')

        return self.factory, self.recipes, self.request

    def test_make_pagination_valid_page(self):
        request_response = self.factory.get(f'{self.request}/?page=2')

        page_obj, pagination_range = make_pagination(request_response, self.recipes, 9)  # noqa: E501;

        self.assertEqual(page_obj.number, 2)

    def test_make_pagination_invalid_page(self):
        request_search = self.factory.get(f'{self.request}/?page=abc')

        page_obj, pagination_range = make_pagination(request_search, self.recipes, 9)  # noqa: E501;

        self.assertEqual(page_obj.number, 1)
