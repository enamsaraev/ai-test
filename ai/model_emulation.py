import pandas as pd
import logging

from dataclasses import dataclass
from typing import Any



@dataclass
class ModelEmulation:
    types_of_model = {
        
    }
    file: str

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        try:
            data = pd.read_csv(f'media/{self.file}')
            df = pd.DataFrame(data=data.head())
            df.to_csv('file_to_save.csv', encoding='utf-8', index=False)
        except UnicodeDecodeError as e:
            logging.error(e)
            return False
        
        return True
        

