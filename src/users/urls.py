from django.urls import path
from .views import sign_up, users, edit_profile


app_name = "users"
urlpatterns = [

    path('', users, name='users'),
    path('update_profile/<id>/', edit_profile, name='edit_profile'),
    path('signup/', sign_up,name="signup")

]
