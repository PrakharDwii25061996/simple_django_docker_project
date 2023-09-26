from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registration, name='register'),
    path('users/list/', views.user_list, name='user_list'),
    path('user/edit/<int:id>/', views.user_edit, name='user_edit'),
    path('user/delete/<int:id>/', views.user_delete, name='user_delete'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
