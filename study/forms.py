from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from notifications_app.models import UserNotificationPreference
from .models import PremiumPlan, PremiumRequest


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    receive_email = forms.BooleanField(
        required=False,
        initial=True,
        label='Nhận thông báo qua email',
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        if get_user_model().objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Email này đã được sử dụng.')
        return email

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            UserNotificationPreference.objects.update_or_create(
                user=user,
                defaults={
                    'receive_email': self.cleaned_data.get('receive_email', True),
                },
            )
        return user


class PremiumRequestForm(forms.ModelForm):
    plan = forms.ModelChoiceField(queryset=PremiumPlan.objects.none(), empty_label=None, widget=forms.RadioSelect, label='Chọn gói Premium')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['plan'].queryset = PremiumPlan.objects.filter(is_active=True)

    class Meta:
        model = PremiumRequest
        fields = ('plan', 'transfer_name', 'transfer_date', 'reference', 'note')
        widgets = {
            'transfer_date': forms.DateInput(attrs={'type': 'date'}),
            'note': forms.Textarea(attrs={'rows': 3}),
        }
