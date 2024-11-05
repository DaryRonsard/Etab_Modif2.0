from django.urls import path, include, re_path
from rest_framework import routers

from api.apiviews.teacher_apiviews import TeacherViewSet
from api.apiviews.student_apiviews import StudentViewSet
from api.apiviews.user_apiviews import UserViewSet
from api.apiviews.adress_apiviews import AdressViewSet

#from api.apiviews.student_apiviews import student_list, student_detail
#from api.apiviews.teacher_apiviews import teacher_list, teacher_detail
#from api.apiviews.user_apiviews import user_list, user_detail
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

routers = routers.DefaultRouter()
routers.register(r'students', StudentViewSet, basename='students'),
routers.register(r'teachers', TeacherViewSet, basename='teachers'),
routers.register(r'users', UserViewSet, basename='users'),
routers.register(r'adress', AdressViewSet, basename='adress'),

#routers.register(r'users', UserViewSet, basename='users'),

#routers.register(r'teachers', teacher_list, basename='teachers')
schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@gsnippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


app_name = 'api'

urlpatterns = [
    #student
    #path('', student_list),
    #path('student/<int:pk>/', student_detail),
    path('', include(routers.urls)),

    #teacher
    #path('teacher_list/', teacher_list),
    #path('teacher/<int:pk>/', teacher_detail),
    #path('teachers/', TeacherViewSet.as_view(routers.urls)),

    #user
    #path('user/', user_list),
    #path('user/<int:id>/', user_detail),



    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
