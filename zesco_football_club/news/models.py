from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __unicode__(self):
        return "%s (%s)" %(self.name, self.email)

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author)
    slug = models.SlugField()
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='news_uploaded_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    # def get_absolute_url(self):
    #     return ('news', [self.slug])

    # def get_absolute_url(self):
    #     return reverse("list")


    def __unicode__(self):
        return "%s (%s)" %(self.title, self.author.name)
