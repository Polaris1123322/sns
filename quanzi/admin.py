from django.contrib import admin
from models import User, Commend, Followship, Share

# Register your models here.
admin.site.register(User)
admin.site.register(Commend)
admin.site.register(Followship)
admin.site.register(Share)