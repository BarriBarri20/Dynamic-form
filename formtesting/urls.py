from django.urls import path, include
from django.views.generic import TemplateView

from .views import  (
    create_course,
    create_session,
    create_assignment,
    create_learningoutcome,
    
    update_course,
    update_session,
    update_assignment,
    update_learningoutcome,
    
    # delete_course,
    delete_session,
    delete_assignment,
    delete_learningoutcome,
)


urlpatterns = [

    path('', TemplateView.as_view(template_name="home.html"), name='create-session'),
    
    path('create-course/', create_course, name='create-course'),
    path('create-session-form/<int:pk>/<int:ck>', create_session, name='create-session-form'),
    path('create-assignment-form/<int:pk>/<int:sk>', create_assignment, name='create-assignment-form'),
    path('create-learningoutcome-form/<int:pk>/<int:sk>', create_learningoutcome, name='create-learningoutcome-form'),
    
    path('update-course/<int:pk>', update_course, name='update-course'),
    path('update-session/<int:pk>', update_session, name='update-session'),
    path('update-assignment/<int:pk>', update_assignment, name='update-assignment'),
    path('update-learningoutcome/<int:pk>', update_learningoutcome, name='update-learningoutcome'),
    
    path('tinymce/', include('tinymce.urls')),
    
    path('create-course/delete-session/<int:pk>', delete_session, name='delete-session'),
    path('create-course/delete-assignment/<int:pk>', delete_assignment, name='delete-assignment'),
    path('create-course/delete-learningoutcome/<int:pk>', delete_learningoutcome, name='delete-learningoutcome')
]