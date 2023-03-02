from django.urls import path, include
from django.views.generic import TemplateView

from .views import  (
    create_session,
    create_session_form,
    detail_session,
    update_session,
    delete_session,
    
    create_assignment,
    create_assignment_form,
    detail_assignment,
    update_assignment,
    delete_assignment,
    
    create_skill,
    create_skill_form,
    detail_skill,
    update_skill,
    delete_skill,

)


urlpatterns = [

    path('', TemplateView.as_view(template_name="home.html"), name='create-session'),
    path('<pk>/', create_session, name='create-session'),
    path('htmx/session/<pk>/', detail_session, name="detail-session"),
    path('htmx/session/<pk>/update/', update_session, name="update-session"),
    path('htmx/session/<pk>/delete/', delete_session, name="delete-session"),
    path('htmx/create-session-form/', create_session_form, name='create-session-form'),
    
    path('<pk>/', create_assignment, name='create-assignment'),
    path('htmx/assignment/<pk>/', detail_assignment, name="detail-assignment"),
    path('htmx/assignment/<pk>/update/', update_assignment, name="update-assignment"),
    path('htmx/assignment/<pk>/delete/', delete_assignment, name="delete-assignment"),
    path('htmx/create-assignment-form/', create_assignment_form, name='create-assignment-form'),
    
    
    path('<pk>/', create_skill, name='create-skill'),
    path('htmx/skill/<pk>/', detail_skill, name="detail-skill"),
    path('htmx/skill/<pk>/update/', update_skill, name="update-skill"),
    path('htmx/skill/<pk>/delete/', delete_skill, name="delete-skill"),
    path('htmx/create-skill-form/', create_skill_form, name='create-skill-form'),
    
]


