from django.contrib import admin
from books.models import Poet, Poem, Comment

#password - ilia

admin.site.register(Poet)
admin.site.register(Poem)
admin.site.register(Comment)