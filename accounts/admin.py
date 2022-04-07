from django.contrib import admin

from .models import User

admin.site.register(User)
admin.site.site_header == "Library Management System"
admin.site.site_title = "Library Management System"
