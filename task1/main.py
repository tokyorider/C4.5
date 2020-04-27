from sys import argv

import pandas as pd

df = pd.read_excel(argv[1], sheet_name='VU')
print(df.to_string())

df = df[df['G_total'].notna() | df['КГФ'].notna()]
df = df.reset_index(drop=True)
print(df.to_string())

attributes = list(df.columns[:-2])
print('Количество атрибутов : ' + str(len(attributes)))
print(attributes)

classes = [pair for pair in zip(df['G_total'], df['КГФ'])]
print('Количество классов : ' + str(len(classes)))
print(classes)
