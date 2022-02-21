import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
df = pd.read_excel('New-2022-ZT_2dLine_Data.xlsx')



df.plot(kind='line', x='AxesSubplot(0.125,0.11;0.775x0.77)')
plt.xlabel('Energy(eV)')
plt.ylabel('Conductance-Value')

plt.grid(True)
plt.show()
