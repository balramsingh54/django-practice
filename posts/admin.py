from django.contrib import admin
from .models import Post

# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "update", "timestamp"]
	list_display_links = ["update"]
	list_editable = ["title"]
	list_filter = ["update", "timestamp"]

	search_fields = ["title", "content"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)