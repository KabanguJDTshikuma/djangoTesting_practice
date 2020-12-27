from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField(max_length=250)
    likes = models.ManyToManyField(User,
            related_name='like', blank=True, default=None)

    
    def get_absolute_url(self):
        return reverse('task1:post_single', args=[self.slug])

    def __str__(self):
        return self.title