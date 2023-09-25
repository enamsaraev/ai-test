from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class ApplicationData(models.Model):
    user = models.ForeignKey(User,
                             related_name='application_forms',
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name=_('Пользователь'))
    gender = models.CharField(max_length=20,
                              verbose_name=_('Пол'))
    surname = models.CharField(max_length=255,
                               verbose_name=_('Фамилия'))
    name = models.CharField(max_length=255,
                            verbose_name=_('Имя'))
    middlename = models.CharField(max_length=255,
                                  null=True,
                                  blank=True,
                                  verbose_name=_('Отчество(при наличии)'))
    birthdate = models.DateField(verbose_name=_('Дата рождения'))
    salary = models.IntegerField(verbose_name=_('Сумма договора, ₽'))


class ImportData(models.Model):
    user = models.ForeignKey(User,
                             related_name='input_datas',
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name=_('Пользователь'))
    file = models.FileField(upload_to='files/',
                            verbose_name=_('Файл (импорт)'))
    model_type = models.CharField(max_length=10,
                                  verbose_name=_('Вид модели (лайт или полная)'))


class PredictData(models.Model):
    import_data = models.ForeignKey('ImportData',
                                    related_name='predicteddatas',
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    verbose_name=_('Ссылка на полученный файл (импорт)'))
    file = models.FileField(upload_to='predicted_files/',
                            verbose_name=_('Обработанные данные'))
    