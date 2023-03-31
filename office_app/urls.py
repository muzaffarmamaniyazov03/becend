from django.urls import path
from .views import *

urlpatterns = [
    path('managements/', ManagementAPIView.as_view()),
    path('regionals/', RegionalAPIView.as_view()),
    path('guides/', GuideAPIView.as_view()),
    path('about/', AboutAPIView.as_view()),
    path('organizations/', OrganizationAPIView.as_view()),
    path('organizations/<int:pk>/', DirectorAPIView.as_view()),
    path('news_pag/', NewsByPagination.as_view()),
    path('news/', NewsAPIView.as_view()),
    path('documents/', DocumentsAPIView.as_view()),
    path('open_data/', OpenDataAPIView.as_view()),

]
