from django.urls import path
from .views import employeeview, employeedetailview
urlpatterns = [
    path("employee/", view=employeeview.as_view()),
    path("employee/<int:id>/", view=employeedetailview.as_view())
]