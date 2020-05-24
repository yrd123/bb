from django.contrib import admin
from .models import Events,EventImages

class EventImagesInline(admin.TabularInline):
    model = EventImages
    extra = 3

class EventImagesAdmin(admin.ModelAdmin):
    inlines = [ EventImagesInline, ]

admin.site.register(Events, EventImagesAdmin)
# Register your models here.
