from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from tasteyourlife.accounts.forms import SignUpForm, UserChangeForm
from tasteyourlife.accounts.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    ordering = ('email',)
    list_display = ['email', 'date_joined', 'last_login']
    list_filter = ()
    form = UserChangeForm
    add_form = SignUpForm
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            'Permissions',
            {
                'fields': (
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),


    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'age')
    exclude = ('user',)
