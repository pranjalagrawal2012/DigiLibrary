from django.contrib import admin
from dlibrary.models import Book, Branch, Feedback, Suser


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_filter = ["course", "branch"]
    list_display = ["name", "course", "branch"]


admin.site.register(Book, BookAdmin)


class BranchAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]


admin.site.register(Branch, BranchAdmin)


class Feedbackadmin(admin.ModelAdmin):
    list_display = ["name", "subject", "message", "user"]
    list_filter = ["name", "user", "subject"]


admin.site.register(Feedback, Feedbackadmin)


class Suseradmin(admin.ModelAdmin):
    list_display = ["name", "user", "city"]
    list_filter = ["name", "user", "city"]


admin.site.register(Suser, Suseradmin)
