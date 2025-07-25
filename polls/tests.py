from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question, Choice

class QuestionTestCase(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)