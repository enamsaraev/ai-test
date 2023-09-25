#                                         пример работы с этим классом
from model_class import *
# from sklearn.metrics import roc_auc_score
mini = False

if mini:
  model = email_model_mini()# создаём объект
else:
  model = email_model() # создаём объект

data = pd.read_csv('ai/datas/clusters1.csv') # загрузка не через sql

# data = pd.read_sql_table('table_name', engine) # загрузка через sql

model_pred = model.predict(data) # получаем предикт

print("_"*100)
print('датасет после обработки:')
print(model.data.head())

model.save_pred() # сохраняем его

print("_"*100)
print('загружаемые данный:')
print(data[["client_id", "target"]].head())
print("_"*100)
# print('roc_auc_score:', roc_auc_score(data['target'], model_pred))
# print("_"*100)