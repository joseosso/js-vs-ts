import pandas as pd
tsm = pd.read_csv('TypeScriptMetrics.csv')
trc = pd.read_csv('TypeScriptReposCharacteristics_gen.csv')

pd.set_option('display.max_columns', None)

for index, row in trc.iterrows():
    trc.at[index, 'ncloc'] = tsm.at[index, 'ncloc']
    trc.at[index, 'cognitive_complexity'] = tsm.at[index, 'cognitive_complexity']
    trc.at[index, 'code_smells'] = tsm.at[index, 'code_smells']

trc.to_csv('TypeScriptReposCharacteristics.csv', index=False)