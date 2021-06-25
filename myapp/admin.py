from django.contrib import admin

# Register your models here.
from . models import User

admin.site.register(User)


admin.site.site_header="DivyaBhasker"

class AdminUser(admin.ModelAdmin):
	list_display=('fname','lname','mobile','email')
	list_filter=('fname',)

	