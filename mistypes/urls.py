
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/submit$', views.submit, name="mistypes_submit"),
]
