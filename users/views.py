from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm, SignupForm
from django.contrib import messages


# Create your views here.
class EmailBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Ivanlid username and password'})
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'users/login.html')


def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            messages.success(request, 'Your profile has been updated!')

            return redirect('update_profile')
        else:
            form = ProfileForm()

    return render(
        request,
        'users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            # 'form': form
        }
    )


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = SignupForm()
    return render(
        request=request,
        template_name='users/signup.html',
        context={
            'form': form
        }
    )

