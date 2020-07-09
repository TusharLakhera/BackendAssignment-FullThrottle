from django.urls import path,include
from UserBackend.views import UserApi,ActivityPeriodApi
from . import views

urlpatterns = [
    path('member/', views.UserApi.as_view()),
    path('activityperiod/', views.ActivityPeriodApi.as_view()),
]
