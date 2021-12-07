from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    caption = CharField(max_length=50, null=True)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    date = models.DateField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='posts', null=True)
    tag = models.ManyToManyField(Tag, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'Post Title : {self.title}  |  Post Author : {self.author}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comment', null=True, blank=True)
    comment_content = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
