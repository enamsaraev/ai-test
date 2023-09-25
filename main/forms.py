from django import forms


class LoginForm(forms.Form):
    """Login form"""
    username = forms.CharField(required=True,
                          widget=forms.TextInput(attrs={
                                'type': 'password',
                                'name': 'password',
                                'class': 'login-form-input login-form-input-username',
                                'placeholder': 'Введите имя пользователя'})
                          )
    password = forms.CharField(empty_value='',
                            required=False,
                            widget=forms.TextInput(attrs={
                                'type': 'password',
                                'name': 'password',
                                'class': 'login-form-input login-form-input-password',
                                'placeholder': 'Введите пароль'})
                            )
    

class ApplicationForm(forms.Form):
    """Application form"""
    gender_mars = forms.CharField(required=False, 
                                  widget=forms.TextInput(attrs={
                                   'id': 'gender-1',
                                   'name': 'gender',
                                   'type': 'radio',
                                   'value': 'Мужчина',
                                   'class': 'tab-content-input-profile-gender',
                                   'tabindex': '-1'})
                                )
    gender_venus = forms.CharField(required=False, 
                                   widget=forms.TextInput(attrs={
                                   'id': 'gender-2',
                                   'name': 'gender',
                                   'type': 'radio',
                                   'value': 'Женщина',
                                   'class': 'tab-content-input-profile-gender',
                                   'tabindex': '-1'})
                                )
    surname = forms.CharField(widget=forms.TextInput(attrs={
                                   'type': 'text',
                                   'class': 'tab-content-input-profile tab-content-input-profile-surname',
                                   'tabindex': '-1',
                                   'placeholder': 'Укажите фамилию',})
                                )
    name = forms.CharField(widget=forms.TextInput(attrs={
                                   'type': 'text',
                                   'class': 'tab-content-input-profile tab-content-input-profile-name',
                                   'tabindex': '-1',
                                   'placeholder': 'Укажите имя',})
                                )
    middlename = forms.CharField(widget=forms.TextInput(attrs={
                                   'type': 'text',
                                   'class': 'tab-content-input-profile tab-content-input-profile-middlename',
                                   'tabindex': '-1',
                                   'placeholder': 'Укажите отчество (при наличии)',})
                                )
    birthdate = forms.DateField(widget=forms.TextInput(attrs={
                                   'type': 'date',
                                   'class': 'tab-content-input-profile tab-content-input-profile-birthdate',
                                   'tabindex': '-1',
                                   'placeholder': 'Укажите дату рождения',})
                                )
    salary = forms.IntegerField(widget=forms.TextInput(attrs={
                                   'type': 'number',
                                   'class': 'tab-content-input-profile tab-content-input-profile-salary',
                                   'tabindex': '-1',
                                   'placeholder': 'Укажите сумму договора, ₽',})
                                )
    

class ImportDataForm(forms.Form):
    CHOICES = (
        ('lite', 'Лайт'),
        ('full', 'Полная')
    )
    # file = forms.FileField(widget=forms.TextInput(attrs={
    #                                'type': 'file',
    #                                'name': 'file',
    #                                'class': 'tab-content-input-file',
    #                                'tabindex': '-1',
    #                                'accept': '.csv,.xlsx',})
    #                             )
    file = forms.FileField()
    model_type = forms.ChoiceField(choices=CHOICES)
                                