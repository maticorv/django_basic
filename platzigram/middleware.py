from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse


class ProfileCompletionMiddleware:
    """
    Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.

    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""

        user = request.user
        path = request.path
        if not request.user.is_anonymous:
            try:
                profile = user.profile
                if not self.profile_have_picture(profile) or not self.profile_have_biography(profile):
                    self.validate_path(path)
            except:
                # logout(request)
                return render(request, 'users/login.html', {'error': 'User has no profile'})

        response = self.get_response(request)
        return response

    def path_is_admin(self, path):
        return path.startswith('/admin/')

    def profile_have_picture(self, profile):
        return True if profile.picture else False

    def profile_have_biography(self, profile):
        return True if profile.biography else False

    def validate_path(self, path):
        if path not in [reverse('update_profile'), reverse('logout')] and self.path_is_admin(path):
            return redirect('update_profile')
