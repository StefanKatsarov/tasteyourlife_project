from enum import Enum

from django.contrib.auth import models as auth_models, password_validation
from django.db import models
from django.utils import timezone

from tasteyourlife.accounts.managers import AppUserManager
from tasteyourlife.common.mixins import ChoicesEnumMixin


class ExperienceLevel(ChoicesEnumMixin, Enum):
    amateur = "Amateur"
    home_cook = 'Home Cook'
    expert = 'Expert'
    professional = 'Professional chef'


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    USERNAME_FIELD = 'email'

    objects = AppUserManager()

    @property
    def user_profile(self):
        profile = Profile.objects.filter(user_id=self.id).get()

        return profile


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=25,
        null=True,
        blank=True
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    experience_level = models.CharField(
        choices=ExperienceLevel.choices(),
        max_length=ExperienceLevel.max_len(),
        null=True,
        blank=True
    )

    about_me = models.TextField(
        blank=True,
        null=True
    )

    photo = models.ImageField(
        upload_to='profile_photos/',
        null=False,
        blank=True,
    )
