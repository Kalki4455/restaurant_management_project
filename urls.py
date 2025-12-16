from django.urls import path
from .views import MenuCategoryListApiView

UrlPatterns = [
    path('api/menu-categories/', MenuCategoryListApiView.as_view(), name='menucategories',)
]