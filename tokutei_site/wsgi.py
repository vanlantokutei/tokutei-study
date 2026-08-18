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

    print(f'[ADMIN-BOOTSTRAP] ADMIN_USERNAME present: {bool(username)}', flush=True)
    print(f'[ADMIN-BOOTSTRAP] ADMIN_EMAIL present: {bool(email)}', flush=True)
    print(f'[ADMIN-BOOTSTRAP] ADMIN_PASSWORD present: {bool(password)}', flush=True)

    if not username or not password:
        print('[ADMIN-BOOTSTRAP] Skipped: ADMIN_USERNAME or ADMIN_PASSWORD is missing.', flush=True)
        return

    try:
        from django.contrib.auth import get_user_model

        User = get_user_model()
        user, created = User.objects.get_or_create(username=username)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        if email:
            user.email = email
        user.set_password(password)
        user.save()

        action = 'created' if created else 'updated'
        print(f'[ADMIN-BOOTSTRAP] SUCCESS: admin account {action} for username={username!r}.', flush=True)
    except Exception as exc:
        print(f'[ADMIN-BOOTSTRAP] ERROR: {type(exc).__name__}: {exc}', flush=True)


_ensure_admin_account()
