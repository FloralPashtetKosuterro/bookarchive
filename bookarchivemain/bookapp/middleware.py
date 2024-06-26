from django.contrib.auth.models import AnonymousUser
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

class BlockedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.is_blocked:
            # Выход пользователя
            request.user.backend = 'django.contrib.auth.backends.ModelBackend'
            request.session.flush()
            request.user = AnonymousUser()

            # Перенаправление на страницу авторизации
            path = reverse('login')
            return HttpResponseRedirect(path)

        response = self.get_response(request)

        return response
