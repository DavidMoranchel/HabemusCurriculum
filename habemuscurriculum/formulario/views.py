from formulario import models as fmodels 
from django.http import HttpResponse
from django.shortcuts import get_object_or_404 , redirect, render
from django.views.generic import View


from users.models import  Skill, ExtendedUser
# Create your views here.


class Get_skills(View):
	def get(self, request):
		template= 'formulario/base.html'
		skills = Skill.objects.all()
		context = {
			'skills':skills,
		}
		return render(request, template, context)

	def post(self, request):
		message = request.POST.get('message','')
		skills = request.POST.getlist('skills','')
		facebook = request.POST.get('facebook','')
		twitter = request.POST.get('twitter','')
		name = request.POST.get('name','')
		github = request.POST.get('github','')
		email = request.POST.get('email','')
		extended_user = ExtendedUser(

				message=message,
				user=request.user,
				facebook=facebook,
				twitter=twitter,
				github=github,
				email=email, 
				name=name,

			)
		extended_user.save()
		for skill_id in skills:
			skill = Skill.objects.get(pk = int(skill_id))
			extended_user.skills.add(skill)

		return redirect("/cuvitae/2")

