"""
WSGI config for tokutei_site project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tokutei_site.settings')

application = get_wsgi_application()


def _ensure_admin_account():
    username = os.environ.get('ADMIN_USERNAME', '').strip()
    email = os.environ.get('ADMIN_EMAIL', '').strip()
    password = os.environ.get('ADMIN_PASSWORD', '')
    if not username or not password:
        return

    try:
        from django.contrib.auth import get_user_model

        User = get_user_model()
        user, _ = User.objects.get_or_create(username=username)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        if email:
            user.email = email
        user.set_password(password)
        user.save()
    except Exception as exc:
        print(f'Admin bootstrap skipped: {exc}')


_ensure_admin_account()
