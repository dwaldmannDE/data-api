"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

from api import views

router = routers.DefaultRouter()
router.register(r'stations', views.StationViewSet)
router.register(r'trains', views.TrainViewSet)
router.register(r'stopovers', views.StopoverViewSet)
router.register(r'remarks', views.RemarkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('station-list/', views.StationListView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui')
]
