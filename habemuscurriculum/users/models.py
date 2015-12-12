from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


def skill_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'skill_{0}/{1}'.format(instance.pk, filename)

# Create your models here.
class Skill(models.Model):
	name = models.CharField(max_length = 50 , null=False)
	img = models.ImageField(upload_to=skill_directory_path)

	def __unicode__(self):
		return self.name

class ExtendedUser(models.Model):
	user = models.OneToOneField(User)
	message = models.TextField(default='')
	skills = models.ManyToManyField(Skill)
	facebook = models.CharField(max_length=50, null=True)
	twitter = models.CharField(max_length=50, null=True)
	github = models.CharField(max_length=50, null=True)
	email = models.CharField(max_length=50, null=True)
	name = models.CharField(max_length=50, null=True)

	def __unicode__(self):
		return self.user.username 



