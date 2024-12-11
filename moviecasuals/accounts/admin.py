from django.contrib import admin
from django.core.exceptions import PermissionDenied

from moviecasuals.accounts.models import MovieUserModel


@admin.register(MovieUserModel)
class MovieUserModelAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'get_roles'
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fields = (
        'username', 'email', 'first_name', 'last_name', 'picture_url', 'is_staff', 'is_active', 'is_superuser',
        'groups', 'get_roles'
    )
    readonly_fields = ('username', 'get_roles',)  # Make username and roles readonly by default
    actions = ['deactivate_users']

    def mark_as_staff(self, request, queryset):
        # Restrict the ability to mark users as staff for redactors
        if not request.user.is_superuser:
            raise PermissionDenied("You do not have permission to mark users as staff.")
        queryset.update(is_staff=True)
        self.message_user(request, "Selected users have been marked as staff.")

    mark_as_staff.short_description = "Mark selected users as staff"

    def deactivate_users(self, request, queryset):
        # Ensure that the redactor cannot deactivate a superuser
        if not request.user.is_superuser:
            queryset = queryset.exclude(is_superuser=True)  # Exclude superusers
        queryset.update(is_active=False)
        self.message_user(request, "Selected users have been deactivated.")

    deactivate_users.short_description = "Deactivate selected users"

    def get_readonly_fields(self, request, obj=None):
        """
        Make fields like 'is_staff', 'is_superuser' and 'groups' readonly for redactors.
        Superusers should be able to edit 'is_superuser'.
        """
        readonly_fields = list(self.readonly_fields)

        if request.user.is_staff and not request.user.is_superuser:
            # For redactors, make 'is_staff', 'is_superuser', and 'groups' read-only
            readonly_fields += ['is_staff', 'is_superuser', 'groups']  # Add these fields to readonly for redactors

        return readonly_fields

    def get_roles(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])

    get_roles.short_description = "Roles"

    def get_model_perms(self, request):
        """
        Restrict the redactor's access to the specific permissions (add/change/delete).
        If the user is staff, we give them permissions for viewing and editing, but not adding staff.
        """
        perms = super().get_model_perms(request)
        if request.user.is_staff:
            perms['view'] = True  # Allow viewing for staff
            perms['change'] = True  # Allow editing for staff
            perms['delete'] = True  # Allow deletion for staff
            perms['add'] = True  # Allow adding normal users only
        return perms

    def get_queryset(self, request):
        """
        Customize the queryset to ensure redactors can only view and modify non-superusers.
        Redactors should not be able to see or delete other staff members.
        """
        queryset = super().get_queryset(request)

        # If the user is a staff member (but not a superuser), exclude other staff members and superusers
        if request.user.is_staff and not request.user.is_superuser:
            queryset = queryset.exclude(is_staff=True)  # Exclude other staff members from being editable/deletable

        return queryset

    def has_delete_permission(self, request, obj=None):
        """
        Restrict delete permissions. Prevent staff from deleting superusers or other staff members.
        """
        if obj is not None and (obj.is_staff or obj.is_superuser) and not request.user.is_superuser:
            # If the user is staff and trying to delete a staff member or superuser, deny permission
            return False
        return super().has_delete_permission(request, obj)