from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', views.StudentViewSet)

urlpatterns = [
    # path('', views.StudentView.as_view()),
    # path('<int:pk>/', views.StudentDetailView.as_view()),
    # path('', views.StudentListCreateView.as_view()),
    # path('<int:pk>/', views.StudentDetailRetrieveUpdateDestroyView.as_view()),
    path('', include(router.urls))
]
