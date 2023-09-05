from .models import User
from django.contrib.auth.admin import UserAdmin
from .models import Post
from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ("pk", "user", "post", "text", "date")
  date_hierarchy = ("date")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ("pk", "title", "description", "image", "user", "date")
  search_fields = ("title", "user")
  date_hierarchy = "date"


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "first_name", "last_name",
                    "email", "is_staff", "is_active",)
    list_filter = ("is_staff", "is_active",)
    fieldsets = (
        ("Base", {"fields": ("email", "password", "username")}),
        ("Permissions", {"fields": ("is_staff",
         "is_active", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "username", "password", "is_staff",
                "is_active", "user_permissions"
            )}
         ),
    )


search_fields = ("email")
ordering = ("email")
