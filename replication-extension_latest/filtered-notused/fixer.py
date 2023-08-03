import pandas as pd
jvsm = pd.read_csv('JavaScriptMetrics.csv')
jsrc = pd.read_csv('JavaScriptReposCharacteristics_gen.csv')

pd.set_option('display.max_columns', None)

for index, row in jsrc.iterrows():
    jsrc.at[index, 'ncloc'] = jvsm.at[index, 'ncloc']
    jsrc.at[index, 'cognitive_complexity'] = jvsm.at[index, 'cognitive_complexity']
    jsrc.at[index, 'code_smells'] = jvsm.at[index, 'code_smells']

jsrc.to_csv('JavaScriptReposCharacteristics.csv', index=False)