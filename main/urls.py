from django.urls import path

from main.views import LoginView, LogoutView, MainPageView, ApplicationFormView, ImportDataView, MainPagePredictedView


app_name = 'main'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('main/', MainPageView.as_view(), name='main_page'),
    path('application_form/', ApplicationFormView.as_view(), name='application_form'),
    path('import_data_form/', ImportDataView.as_view(), name='import_data_form'),
    path('predicted_main/', MainPagePredictedView.as_view(), name='predicted_main'),
]