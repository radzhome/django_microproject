from django.conf.urls import url  # include, url

urlpatterns = [
    url(r'^$', 'django_microproject.views.home', name='home'),
]
