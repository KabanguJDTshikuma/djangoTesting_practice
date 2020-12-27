from django.test import TestCase
from task1.models import Post
from django.contrib.auth.models import User

class TestAppModels(TestCase):
    def test_model_str(self):
        title = Post.objects.create(title="Django Testing", content="This is the content")
        self.assertEqual(str(title), "Django Testing")

    def test_post_like_users(self):
        testuser = User.objects.create(username='testuser', password='1234')
        testuser2 = User.objects.create(username='testuser2', password='1234')
        title = Post.objects.create(title="django", content="New content")
        title.likes.set([testuser.pk, testuser2.pk])
        self.assertEqual(title.likes.count(), 2)