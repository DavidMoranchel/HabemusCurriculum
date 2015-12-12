from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect

from users.models import ExtendedUser

# Create your views here.
class UserView(View):
	def get(self, request, user):
		template  = 'users/user.html'
		extended_user = ExtendedUser.objects.get(user=user)
		context = {
			'extended_user': extended_user
		}

		return render(request, template, context)
