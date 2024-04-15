from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from staff.models import Profile  # Assuming your Profile model is in the staff app

def profile(request, slug):
    # Fetch the profile based on the slug or return a 404 error if not found
    profile = get_object_or_404(Profile, slug=slug)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Optionally, you can add a success message
        messages.success(request, 'Your message was successfully submitted!')

        # Redirect to the same page or another page
        return redirect(reverse('profile', kwargs={'slug': slug}))

    context = {
        'profile': profile,  # Pass the profile object to the context
    }
    return render(request, 'index4.html', context)

