from django.shortcuts import redirect
from django.contrib import messages


class AccessControlMixin:
    DENIED_MESSAGE = ""

    def get_user_attribute(self):

        return 'user'

    def has_permission(self, user, obj, user_attribute):
        """
        Check if the user has permission to access the given object.
        Redactors (staff but not admin) are restricted from editing accounts and comments.
        """
        if user.is_superuser:
            return True

        if user.is_staff:

            if 'Content Approver' in [group.name for group in user.groups.all()]:

                if user_attribute == 'movie' or user_attribute == 'director':
                    return True
                elif user_attribute == 'comment':

                    if obj.user == user:
                        return True
                    return False

            if 'Admins' in [group.name for group in user.groups.all()]:

                return True


        if user_attribute == 'self':
            return obj == user

        return getattr(obj, user_attribute) == user

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





