from django.urls import path, include

from tasteyourlife.accounts.views import profile_edit, SignUpView, SignOutView, ProfileView, SignInView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('profile/<int:pk>/', include([
        path('', ProfileView.as_view(), name='profile details'),
        path('edit/', profile_edit, name='profile edit')
    ]))
]
