from django.urls import path, include
from rest_framework_nested import routers
from .views import ProductViewSet, ReviewViewSet
from .views import ProductViewSet, ReviewViewSet, RegisterView, CustomAuthToken




router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)

product_router = routers.NestedSimpleRouter(router, r'products', lookup='product')
product_router.register(r'reviews', ReviewViewSet, basename='product-reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
      path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
]
