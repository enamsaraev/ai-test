import pandas as pd
import logging
import csv

from dataclasses import dataclass
from typing import Any

from django.contrib.auth.models import User
from django.core.files import File
from django.contrib.auth.models import User

from dbcore.models import ApplicationData, ImportData, PredictData
from ai.model_emulation import ModelEmulation


@dataclass
class ApplicationHelper:
    data: dict
    user: User

    def __call__(self, *args: Any, **kwds: Any) -> ApplicationData:
        self._normilize_data()
        return self._save_form()
    
    def _normilize_data(self) -> None:
        self.data['gender'] = self.data['gender_mars'] if self.data['gender_mars'] else self.data['gender_venus']
        self.data.pop('gender_mars')
        self.data.pop('gender_venus')

    def _save_form(self) -> ApplicationData:
        return ApplicationData.objects.create(user=self.user ,**self.data)
    

@dataclass
class ImportDataHelper:
    data: dict
    user: User

    def __call__(self, *args: Any, **kwds: Any) -> ImportData:
        return self._save_form()
    
    def _save_form(self) -> ImportData:
        return ImportData.objects.create(user=self.user, **self.data)
    

@dataclass
class AIModel:
    import_file: ImportData

    def __call__(self, *args: Any, **kwds: Any) -> None:
        result = ModelEmulation(file=self.import_file.file)()
        if result:
            with open('file_to_save.csv', mode='rb') as f:
                PredictData.objects.create(import_data=self.import_file, file=File(f, name=f'predicted-{self.import_file.file}'))


@dataclass
class PredictedModelHelper:
    user: User

    def __call__(self, *args: Any, **kwds: Any) -> list:
        obj = self._get_predicted_data()
        if not obj:
            return False
        
        df = self._read_file(obj=obj)
        if df.empty:
            return False

        return self._parse_data(df=df)
    
    def _get_predicted_data(self) -> PredictData:
        return PredictData.objects.filter(import_data__user=self.user).last()
    
    def _read_file(self, obj: PredictData) -> pd.DataFrame:
        try:
            data = pd.read_csv(f'media/{obj.file}')

        except Exception as e:
            logging.error(e)
            return None

        df = pd.DataFrame(data=data)
        return df
    
    def _parse_data(self, df: pd.DataFrame) -> list:
        parsed_data = []
        for _, row in df.iterrows():
            parsed_data.append(row.values.flatten().tolist())
        
        return parsed_data
