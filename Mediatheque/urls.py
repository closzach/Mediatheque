"""
URL configuration for Mediatheque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('livres/', include('livres.urls', 'livres')),
    path('', hub, name='hub'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('account/', account, name='account'),
    path('account/edit/', modifier_utilisateur, name='modifier_account'),
    path('account/change_password/', change_password, name='change_password'),
    path('account/delete/', supprimer_account, name='supprimer_account'),
    path('groups/', group_list, name='group_list'),
    path('manage-group-users/<int:group_id>/', manage_group_users, name='manage_group_users'),
    path('add-user-to-group/<int:group_id>/<int:user_id>/', add_user_to_group, name='add_user_to_group'),
    path('remove-user-from-group/<int:group_id>/<int:user_id>/', remove_user_from_group, name='remove_user_from_group'),
    path('ajax-toggle-user-group/<int:group_id>/<int:user_id>/', ajax_toggle_user_group, name='ajax_toggle_user_group'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
