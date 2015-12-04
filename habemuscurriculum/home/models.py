from django.db import models
from django_markdown.models import MarkdownField
from autoslug import AutoSlugField

# Create your models here.

class Entry(models.Model):
	title = models.CharField(max_length = 140)
	content = MarkdownField()
	slug = AutoSlugField(unique=True, populate_from='title')
	publish = models.BooleanField(default = True)
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	def __str__(self):
		return "{} - {}".format(self.title, self.modified)
