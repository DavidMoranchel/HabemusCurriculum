from django.contrib import admin

# Register your models here.
from .models import Skill,SkillUser,ExtendedUser

admin.site.register(Skill)
admin.site.register(ExtendedUser)
admin.site.register(SkillUser)