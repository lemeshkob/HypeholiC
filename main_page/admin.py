from django.contrib import admin
from main_page.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)