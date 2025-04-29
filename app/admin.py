from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import CoMentor, Mentorship, UserProfile


class MentorshipAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "company",
        "status",
        "user",
        "comentor",
        "created_at",
        "update_at",
    )
    list_filter = ("status", "company")
    search_fields = ("name", "company", "user__username")
    date_hierarchy = "created_at"
    ordering = ("created_at",)
    readonly_fields = ("created_at", "update_at")


class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )
    search_fields = ("email",)
    list_display = ("username", "email", "is_staff", "is_active")
    ordering = ("email",)
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")


admin.site.register(CoMentor)
admin.site.register(UserProfile, CustomUserAdmin)
admin.site.register(Mentorship, MentorshipAdmin)
