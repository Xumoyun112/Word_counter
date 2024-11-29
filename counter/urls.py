from django.urls import path

from counter import views

app_name = 'counter'

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
]
