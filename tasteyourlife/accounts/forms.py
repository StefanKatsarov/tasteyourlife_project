from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from tasteyourlife.accounts.models import Profile

UserModel = get_user_model()


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=commit)
        user.set_password(self.cleaned_data["password1"])
        profile = Profile(
            user=user
        )
        if commit:
            user.save()
            profile.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserModel
        fields = ('email', 'password',)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'experience_level', 'about_me', 'photo')

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': "form-control"
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': "form-control"
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': "form-control"
                }
            ),
            'experience_level': forms.Select(
                attrs={
                    'class': "form-control"
                }
            ),
            'about_me': forms.Textarea(
                attrs={
                    'class': "form-control"
                }
            ),
            'photo': forms.FileInput(
                attrs={
                    'class': "form-control"
                }
            ),
        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"

