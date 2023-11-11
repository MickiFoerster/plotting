import plotly.express as px
import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.sin(x)

fig = px.line(x=x, y=y, title='sin(x) Function', labels={'x': 'x', 'y': 'sin(x)'})
fig.show()

