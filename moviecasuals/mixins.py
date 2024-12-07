from django.shortcuts import redirect
from django.contrib import messages


class AccessControlMixin:
    DENIED_MESSAGE = "Sorry, you are not authorized to view this content."

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if not (obj.user == request.user or request.user.is_superuser or request.user.is_staff):
            messages.error(request, self.DENIED_MESSAGE)
            return redirect('access-control')
        return super().get(request, *args, **kwargs)

