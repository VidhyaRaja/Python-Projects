from django.contrib import admin
from demo.models import Site 
from demo.models import Group 
from demo.models import Search 

# Register your models here.
class SiteAdmin(admin.ModelAdmin):
    list_display = ["name", "url", "image", "group"]
class SearchAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "urlPartBeforeKeywords", "urlPartAfterKeywords"]
admin.site.register(Site, SiteAdmin)
admin.site.register(Search, SearchAdmin)
admin.site.register(Group)
