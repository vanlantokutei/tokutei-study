from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import UserNotificationPreference


@login_required
def email_settings(request):
    preference, _ = UserNotificationPreference.objects.get_or_create(
        user=request.user,
        defaults={'receive_email': True},
    )

    saved = False
    if request.method == 'POST':
        preference.receive_email = request.POST.get('receive_email') == 'on'
        preference.save(update_fields=['receive_email', 'updated_at'])
        return redirect('/email-settings/?saved=1')

    if request.GET.get('saved') == '1':
        saved = True

    return render(request, 'notifications_app/email_settings.html', {
        'preference': preference,
        'saved': saved,
    })
