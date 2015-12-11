from __future__ import unicode_literals
from django.db import models
from django import forms
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
	message = models.TextField()
	skills = models.ManyToManyField(Skill, through='SkillUser')

	def __unicode__(self):
		return self.user.username 


class SkillUser(models.Model):
	experience= models.TextField()
	skills = models.ForeignKey('Skill', null=False)
	user = models.ForeignKey(ExtendedUser, null=False)
	facebook = models.CharField(max_length=50, null=True)
	twitter = models.CharField(max_length=50, null=True)
	github = models.CharField(max_length=50, null=True)
	email = models.CharField(max_length=50, null=True)

	def __unicode__(self):
		return self.user.user.username 

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
	


