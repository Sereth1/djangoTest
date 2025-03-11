from django.urls import path
from .views import home_page_view,sub_page

urlpatterns = [
path("", home_page_view),
path('sub',sub_page)
]
