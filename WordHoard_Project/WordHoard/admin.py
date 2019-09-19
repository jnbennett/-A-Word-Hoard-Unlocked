from django.contrib import admin
from .models import Text, Author, Translator

admin.site.register(Text)
admin.site.register(Author)
admin.site.register(Translator)

