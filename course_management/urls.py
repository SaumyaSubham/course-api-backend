from django.urls import path
from django.shortcuts import redirect
from course import views

urlpatterns = [
    path('', lambda request: redirect('courses')),  # Redirect to /api/courses
    path('api/courses', views.courses, name='courses'),
    path('api/courses/<int:pk>', views.course_detail, name='course_detail'),
    path('api/instances', views.create_instance, name='create_instance'),
    path('api/instances/<int:year>/<int:semester>', views.list_instances, name='list_instances'),
    path('api/instances/<int:year>/<int:semester>/<str:course_id>', views.instance_detail, name='instance_detail'),
]