# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# Изначально делал в Google Colab

# Решение с использованием "one hot"

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
one_hot = pd.get_dummies(data['whoAmI'], prefix='whoAmI')
data = pd.concat([data, one_hot], axis=1)
data.drop('whoAmI', axis=1, inplace=True)
data.head()

# Решение "без" использования "one hot"

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
unique_values = data['whoAmI'].unique()
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)
data.drop('whoAmI', axis=1, inplace=True)
data.head()