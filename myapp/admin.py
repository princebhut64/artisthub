from django.contrib import admin
from . models import *
# Register your models here.
admin.site.site_header = "Artist Hub"
admin.site.index_title = "Welcome to Artist Hub"
admin.site.site_title = "Artist Hub"
admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Events)
admin.site.register(Contact)
admin.site.register(Team)
admin.site.register(BookArtist)
admin.site.register(Newsletter)







