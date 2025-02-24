from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile

def edit_profile(request):
    # Get the user profile if it exists, otherwise create a new one
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after successful edit
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'form': form})
