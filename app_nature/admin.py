from django.contrib import admin
from. models import peaks, mountain, texts_on_website, Profile, posts

# Register your models here.

class peaksAdmin(admin.ModelAdmin):
    list_display = ('name_of_mountain', 'name', 'height')
admin.site.register(peaks, peaksAdmin)
admin.site.register(mountain)
admin.site.register(texts_on_website)
admin.site.register(Profile)

class postsAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_date')
admin.site.register(posts, postsAdmin)



