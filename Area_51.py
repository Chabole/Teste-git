import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ZebraLib as zb
from scipy import stats

df_0 = pd.read_excel('D:/UNESP/7 semestre - Eng/Lab. Mec. Flu/Relatório 3 - Dados.xlsx', 
sheet_name='Carregamento')

df_1 = pd.read_excel('D:/UNESP/7 semestre - Eng/Lab. Mec. Flu/Relatório 3 - Dados.xlsx', 
sheet_name='Descarrega')

ref = list(df_0['Referencia']) + list(df_1['Referencia'])
calib = list(df_0['Calibrar']) + list(df_1['Calibrar'])

poly= zb.fit(ref, calib, 1)
p = np.polyfit(ref, calib, 1)

slope, intercept, r_value, p_value, std_err = stats.linregress(ref, calib)

fig, ax = plt.subplots()
ax.set(ylabel= 'Calibrar [psi]', xlabel='Referencia [psi]')

ax.scatter(ref, calib, color='red', label='Dados')
ax.plot(ref, poly(ref), color='blue', linestyle=':', 
    label='Equação' + f' p(x)={p[0]:.3f}x - {abs(p[1]):.3f}' + r', $R^{2}=$' + f'{r_value:.3f}')

zb.setup(ax, (0, 100), (0, 100))

fig.savefig('D:/Dados_2.pdf', bbox_inches='tight')


