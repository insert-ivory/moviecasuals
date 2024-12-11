from django.shortcuts import redirect
from django.contrib import messages


class AccessControlMixin:
    DENIED_MESSAGE = ""

    def get_user_attribute(self):
        # Default to 'user', but allow subclasses to specify their own user attribute
        return 'user'

    def has_permission(self, user, obj, user_attribute):
        """
        Check if the user has permission to access the given object.
        Redactors (staff but not admin) are restricted from editing accounts and comments.
        """
        if user.is_superuser:
            return True  # Superusers can access everything

        if user.is_staff:
            # Check if the user is a redactor or admin
            if 'Content Approver' in [group.name for group in user.groups.all()]:
                # Redactors (Content Approvers) can access movie-related objects
                if user_attribute == 'movie' or user_attribute == 'director':
                    return True
                elif user_attribute == 'comment':
                    # Redactors can only access their own comments
                    if obj.user == user:
                        return True
                    return False  # Redactors can't access other people's comments

            if 'Admins' in [group.name for group in user.groups.all()]:
                # Admins can access everything
                return True

        # If it's neither a redactor nor admin, allow access based on user attribute
        if user_attribute == 'self':
            return obj == user  # Only allow access to their own data

        return getattr(obj, user_attribute) == user  # Allow if the object belongs to the user

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        user_attribute = self.get_user_attribute()
        user = request.user

        if not self.has_permission(user, obj, user_attribute):
            messages.error(request, self.DENIED_MESSAGE)
            return redirect('access-control')

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        user_attribute = self.get_user_attribute()
        user = request.user

        if not self.has_permission(user, obj, user_attribute):
            messages.error(request, self.DENIED_MESSAGE)
            return redirect('access-control')

        return super().post(request, *args, **kwargs)





