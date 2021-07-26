from django.urls import path
from .views import pics

app_name = "picmix"
urlpatterns = [

    path('', pics, name='upload'),

]
