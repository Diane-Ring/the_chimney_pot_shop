from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):

    def test_form_is_valid(self):
        review_form = ReviewForm({
            'title': 'Great quality',
            'rating': 5,
            'body': 'This is a great post'
        })
        self.assertTrue(review_form.is_valid(), msg='Form is not valid')
