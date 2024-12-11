from django.contrib import admin

from moviecasuals.director.models import Director


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'approved', 'user', 'picture_available')
    search_fields = ('first_name', 'last_name', 'biography', 'user__username')
    list_filter = ('approved', 'date_of_birth')
    fields = ('first_name', 'last_name', 'date_of_birth', 'biography', 'picture_url', 'user', 'approved')
    actions = ['approve_directors', 'revoke_approval']
    readonly_fields = ('full_name',)

    def full_name(self, obj):
        return obj.get_full_name()

    full_name.short_description = "Full Name"

    def approve_directors(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, "Selected directors have been approved.")

    approve_directors.short_description = "Approve selected directors"

    def revoke_approval(self, request, queryset):
        queryset.update(approved=False)
        self.message_user(request, "Approval revoked for selected directors.")

    revoke_approval.short_description = "Revoke approval for selected directors"

    def picture_available(self, obj):
        return bool(obj.picture_url)

    picture_available.short_description = "Picture Available"
    picture_available.boolean = True