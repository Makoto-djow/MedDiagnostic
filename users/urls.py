from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView

from users.views import (
    UserCreateView,
    email_verification,
    AppointmentListView,
    AppointmentDetailView,
    AppointmentCreateView,
    AppointmentUpdateView,
    AppointmentDeleteView,
)


app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email_confirm/<str:token>/', email_verification, name='email_confirm'),

    path("appointment_list/", AppointmentListView.as_view(), name="appointment_list"),
    path("appointment_detail/<int:pk>/", AppointmentDetailView.as_view(), name="appointment_detail"),
    path("appointment_create/create", AppointmentCreateView.as_view(), name="appointment_create"),
    path(
        "appointment_update/<int:pk>/update/", AppointmentUpdateView.as_view(), name="appointment_update"
    ),
    path(
        "appointment_delete/<int:pk>/delete", AppointmentDeleteView.as_view(), name="appointment_delete"
    ),

]
