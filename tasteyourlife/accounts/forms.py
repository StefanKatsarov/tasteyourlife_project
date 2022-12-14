from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from tasteyourlife.accounts.models import Profile

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            user=user,
        )

        if commit:
            profile.save()

        return user
