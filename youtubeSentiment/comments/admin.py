from django.contrib import admin
from .models import Videos, Comments, Author, Channel
# Register your models here.
admin.site.register(Videos)
admin.site.register(Comments)
admin.site.register(Author)
admin.site.register(Channel)
