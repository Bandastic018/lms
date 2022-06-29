from django.contrib import admin

from .models import Choices, Question

# Register your models here.


admin.site.register(Question)
admin.site.register(Choices)
