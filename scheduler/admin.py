from django.contrib import admin
from .models import DummyUser, DateRecord


@admin.register(DummyUser)
class DummyUserAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "email",
    )

    search_fields = (
        "name",
        "email",
    )


@admin.register(DateRecord)
class DateRecordAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "datetime_value",
        "timezone",
    )

    list_filter = (
        "timezone",
    )

    search_fields = (
        "timezone",
    )