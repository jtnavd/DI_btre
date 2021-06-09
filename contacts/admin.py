from django.contrib import admin
# from django.apps import apps
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','listing','email','contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25

# admin.site.register(Contact, ContactAdmin)

# models = apps.get_models()
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass
