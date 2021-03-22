from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


# class CustomUserAdmin(admin.ModelAdmin):
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    # 최초 실습했떤 custom 코드들
    # list_display = ("username", "email", "gender", "language", "currency", "superhost")
    # list_filter = (
    #     "language",
    #     "currency",
    #     "superhost",
    # )


# 위의 @admin.register(models.User) 라고 해 놓은건 Decorator 인데 아래처럼 하는것과 동일한 효과다.
# admin.site.register(models.User, CustomUserAdmin)