import matplotlib.pyplot as plt
import pandas as p
df = pd.read_excel('/content/Datavisualization.xlsx')
df['FuelType'].value_counts().plot(kind="bar",xlabel='Fuel
type',ylabel='Count')
plt.show()
