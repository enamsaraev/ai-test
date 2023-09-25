from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

from main.forms import LoginForm, ApplicationForm, ImportDataForm
from main.helpers import ApplicationHelper, ImportDataHelper, AIModel, PredictedModelHelper


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        ctx = {
            'user': request.user,
            'application_form': ApplicationForm(),
            'import_data_form': ImportDataForm(),
        }
        return render(request, 'index.html', context=ctx)
    

class MainPagePredictedView(View):
    def get(self, request, *args, **kwargs):
        ctx = {
            'user': request.user,
            'application_form': ApplicationForm(),
            'import_data_form': ImportDataForm(),
            'predicted_data': PredictedModelHelper(request.user)()
        }
        return render(request, 'index.html', context=ctx)
    

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        ctx = {
            'form': form
        }
        return render(request, 'login.html', context=ctx)
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user=user)
                return redirect('main:main_page')

        return render(request, 'login.html', context={'form': LoginForm()})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main:login')
    

class ApplicationFormView(View):
    def post(self, request, *args, **kwargs):
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            app = ApplicationHelper(data=form.cleaned_data, user=request.user)()
            print(app)
        return redirect('main:main_page')
    

class ImportDataView(View):
    def post(self, request, *args, **kwargs):
        form = ImportDataForm(request.POST, request.FILES)
        if form.is_valid():
            import_file = ImportDataHelper(data=form.cleaned_data, user=request.user)()
            AIModel(import_file=import_file)()
        return redirect('main:predicted_main')
    

