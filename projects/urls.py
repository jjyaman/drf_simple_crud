from django.urls import path
from .views import ProjectsListAPIView, ProjectsCreateAPIView, ProjectsRetrieveAPIView, ProjectsUpdateAPIView, ProjectsDestroyAPIView

urlpatterns = [
    path('projects/list/', ProjectsListAPIView.as_view(), name='projects'),
    path('projects/create/', ProjectsCreateAPIView.as_view(), name='projects_create'),
    path('projects/retrieve/<str:pk>/', ProjectsRetrieveAPIView.as_view(), name='projects_retrieve'),
    path('projects/update/<str:pk>/', ProjectsUpdateAPIView.as_view(), name='projects_update'),
    path('projects/destroy/<str:pk>/', ProjectsDestroyAPIView.as_view(), name='projects-destroy')
]