from django.shortcuts import render
from django.views.generic import View

from users.models import ExtendedUser

# Create your views here.
class UserView(View):
	def get(self, request, username):
		#Poner template
		template  = ''
		extended_user = ExtendedUser.objects.get(user__username=username)
		context = {
			'extended_user': extended_user
		}

		return render(request, template, context)
