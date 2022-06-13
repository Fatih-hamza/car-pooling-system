from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home_core),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('profile/', views.profile),
    path('conducteur_profile/<int:id>', views.conducteur_profile),
    path('update_profile/', views.update_profile),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)