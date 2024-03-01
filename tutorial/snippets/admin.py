from django.contrib import admin
from .models import Snippet

#Напомним, что выделенное поле автоматически устанавливается нашим пользовательским (Admin)
class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = ("highlighted",)


admin.site.register(Snippet, SnippetAdmin)