import joblib
import pandas as pd
import os
import sqlite3

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# cursor.execute("INSERT INTO database VALUES ('client_id', 'predict')")

class email_model():

    def __init__(self):  # инициализация
        self.model = joblib.load(os.path.join(BASE_DIR, 'ai/trained_models/XgbClassifier.joblib'))  # загрузка обученной модели из файла
        self.drop_columns = ['report_date']
        # best_columns это колонки для обработки датасета

    def predict(self, df):  # обработка данных + сохранения ответа
        df["Year"] = pd.to_datetime(df["report_date"]).dt.year
        df["Month"] = pd.to_datetime(df["report_date"]).dt.month
        df["Day"] = pd.to_datetime(df["report_date"]).dt.day

        df = df.drop(columns=self.drop_columns)
        df.fillna(0, inplace=True)
        try:
            df = df.drop(columns='target')
        except:
            df = df
        pred = self.model.predict_proba(df)
        self.data = df
        self.pred = pred
        # return pred[:, 1]
        self.save_pred()

    def save_pred(self):  # пихаем заполненный датасет куда либо
        self.data["target"] = self.pred[:, 1]
        self.data[["client_id", "target"]].sort_index().to_csv('file_to_save.csv', index=False)  # загрузка в файл

        # self.data.to_sql('table_name', engine, if_exists='replace', index=False) #  загрузка в sql таблицу

        # return self.df # ну или можно возвращать датасет


class email_model_mini(email_model):

    def __init__(self):  # инициализация
        self.model = joblib.load(os.path.join(BASE_DIR, 'ai/trained_models/lgbClassifier.joblib'))  # загрузка обученной модели из файла
        self.best_columns = ['col2468', 'col2470', 'client_id', 'Month', 'col2663', 'col2661', 'col2436', 'col2565',
                             'col2564', 'col2660', 'col2222', 'col2216', 'col2310', 'col2412', 'col2316', 'col2214',
                             'col2437', 'col2317', 'col2588', 'col2388']
        # best_columns это колонки для обработки датасета

    def predict(self, df):  # обработка данных + сохранения ответа
        df["Year"] = pd.to_datetime(df["report_date"]).dt.year
        df["Month"] = pd.to_datetime(df["report_date"]).dt.month
        df["Day"] = pd.to_datetime(df["report_date"]).dt.day

        df = df[self.best_columns]

        df.fillna(0, inplace=True)
        try:
            df = df.drop(columns='target')
        except:
            df = df

        pred = self.model.predict_proba(df)
        self.data = df
        self.pred = pred
        # return pred[:, 1]
        self.save_pred()

    def save_pred(self):  # пихаем заполненный датасет куда либо

        self.data["target"] = self.pred[:, 1]
        self.data[["client_id", "target"]].sort_index().to_csv('file_to_save.csv', index=False)  # загрузка в файл

        # self.data.to_sql('table_name', engine, if_exists='replace', index=False) #  загрузка в sql таблицу

        # return self.df # ну или можно возвращать датасет