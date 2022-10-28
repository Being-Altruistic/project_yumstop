from django.contrib import admin
from .models import Post , dieticians , appointments
# Register your models here. To show up on admin page

admin.site.register(Post)
admin.site.register(dieticians)
admin.site.register(appointments)