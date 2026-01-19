from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import ReviewForm
from .models import Product

class TestProductsViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.product = Product(title="products title",
                         slug="products-title",
                         content="products content", status=1)
        self.product.save()

    def test_render_product_detail_page_with_review_form(self):
        response = self.client.get(reverse(
            'product_detail', args=['products-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"products title", response.content)
        self.assertIn(b"products content", response.content)
        self.assertIsInstance(
            response.context['review_form'], ReviewForm)
        
    def test_successful_review_submission(self):
        """Test for posting a review on a product"""
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test review.'
        }
        response = self.client.post(reverse(
            'product_detail', args=['products-title']), post_data, follow=True)

        # The view redirects after successful post; follow=True should land on 200
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Review submitted and awaiting approval',
            response.content
        )
