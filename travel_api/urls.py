from django.urls import include, path
from rest_framework import routers
from core import views
from django.conf.urls import include, url
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'amounts', views.AmountViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^search/', views.SearchView.as_view()),
]
urlpatterns += router.urls