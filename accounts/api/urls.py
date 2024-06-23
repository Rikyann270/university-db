from django.urls import path

from accounts.api.views import(
    registration_view,
    update_account_view,
    account_properties_view,
    login_view,

)
from rest_framework.authtoken.views import obtain_auth_token

app_name = "accounts"


urlpatterns = [
        path('register', registration_view, name="register"),
        path('login', login_view, name="login"),
        path('update_account', update_account_view, name="update_account"),
        path('account_properties', account_properties_view, name="account_properties"),
]