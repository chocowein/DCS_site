from django.urls import path
# blog ディレクトリの中の views.py を import
from DCS_app import views
from .views import upload_image

urlpatterns = [
    # views.py の index() 関数を呼び出す
    path('', views.upload_image),
]
