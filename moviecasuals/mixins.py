from django.shortcuts import redirect
from django.contrib import messages


class AccessControlMixin:
    DENIED_MESSAGE = ""

    def get_user_attribute(self):
        # Default to 'user', but allow subclasses to specify their own user attribute
        return 'user'

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        user_attribute = self.get_user_attribute()
        user = request.user

        if user_attribute == 'self':
            if not (obj == user or user.is_superuser or user.is_staff):
                messages.error(request, self.DENIED_MESSAGE)
                return redirect('access-control')
        else:
            if not (getattr(obj, user_attribute) == user or user.is_superuser or user.is_staff):
                messages.error(request, self.DENIED_MESSAGE)
                return redirect('access-control')

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        user_attribute = self.get_user_attribute()
        user = request.user

        if user_attribute == 'self':
            if not (obj == user or user.is_superuser or user.is_staff):
                messages.error(request, self.DENIED_MESSAGE)
                return redirect('access-control')
        else:
            if not (getattr(obj, user_attribute) == user or user.is_superuser or user.is_staff):
                messages.error(request, self.DENIED_MESSAGE)
                return redirect('access-control')

        return super().post(request, *args, **kwargs)




