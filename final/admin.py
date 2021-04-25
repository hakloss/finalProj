from django.contrib import admin
from scheduler.models import user, course, lab, section
# Register your models here.
admin.site.register(user)
admin.site.register(course)
admin.site.register(lab)
admin.site.register(section)