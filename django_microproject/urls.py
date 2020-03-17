from django.urls import path
from django_microproject import views

urlpatterns = [
    path(r'', views.home, name='home'),
    # re_path(r'^$', 'django_microproject.views.home', name='home'),
    # path(r'', include('identity.urls')),
]
