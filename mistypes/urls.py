
from django.conf.urls import url

from . import views

app_name = "mistypes"

urlpatterns = [
    url(r'^/submit$', views.submit, name="mistypes_submit"),
]
