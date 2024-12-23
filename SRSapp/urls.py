from .views import *
from django.urls import path
from rest_framework_simplejwt.views import *


urlpatterns = [

    # endpoints for login and logout
    path('login/', TokenObtainPairView.as_view()), 
    path('refresh/', TokenRefreshView.as_view()),
    path('logout/', TokenBlacklistView.as_view()),

    # plot endpoints
    path("plot/" , manage_plot),
    path('plot/<int:id>/', manage_plot),


    # payment endpoints
    path('payment/', manage_payment),
    path('payment/<int:id>/', manage_payment),

    # user endpoint
    path('user/', manage_user),
    path('user/<int:id>/', manage_user),


]
