from django.contrib import admin

from .models import AboutMe


# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    exclude = ('body_after_changed',)


admin.site.register(AboutMe, MyModelAdmin)  # admin.site.register()方法的第一个参数应该是模型类,第二个参数是模型管理类。
