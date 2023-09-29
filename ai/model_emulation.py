import pandas as pd
import logging

from dataclasses import dataclass
from typing import Any

from ai.model_class import email_model, email_model_mini

@dataclass
class ModelEmulation:
    types_of_model = {
        'full': email_model,
        'lite': email_model_mini
    }
    file: str
    form_type: str

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        data = self._read_file()
        if data.empty or None:
            return False

        model = self.types_of_model[self.form_type]()
        model.predict(data)

        return True
    
    def _read_file(self):
        data = None
        try:
            data = pd.read_csv(f'media/{self.file}')
        except UnicodeDecodeError as e:
            logging.error(e)
        
        return data

# df = pd.DataFrame(data=data.head())
# df.to_csv('file_to_save.csv', encoding='utf-8', index=False)