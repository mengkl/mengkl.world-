from django.contrib import admin

from passage.models import Passage, Tag


# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    exclude = ('abstract_after_changed',)


admin.site.register(Tag)
admin.site.register(Passage, MyModelAdmin)

