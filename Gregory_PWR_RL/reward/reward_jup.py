import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from reward import Reward as rwd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import plot as pplot



# Plots for 1 limit criterion and 1 maximized criterion

dict1={'type': 'sum_linear',
     'number_limit_criteria': 1,
     'number_maximum_criteria': 1,
     'L1': (1.48,1/2),
     'M1': (14.608,1/2)}
R1 = rwd(dict1)

dict2={'type': 'sum_exponential',
     'number_limit_criteria': 1,
     'number_maximum_criteria': 1,
     'L1': (1.48,1/2),
     'M1': (14.608,1/2)}
R2 = rwd(dict2)



nd = 100

# 3D Figures plotting

fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=("sum_linear before limit", "sum_exponential before limit", 
                    "sum_linear after limit", "'sum_exponential after limit",
                   'sum_linear limit', 'sum_exponential limit'),
    specs=[[{'type': 'surface'}, {'type': 'surface'}], 
           [{'type': 'surface'}, {'type': 'surface'}],
           [{'type': 'surface'}, {'type': 'surface'}]])

c1 = np.linspace(0.5,1.48,nd)
c2 = np.linspace(10,20,nd)

Z1 = np.zeros((nd,nd))
Z2 = np.zeros((nd,nd))
for i in range(nd):
    for j in range(nd):
        Z1[j,i] = R1.evaluate([c1[i], c2[j]])
        Z2[j,i] = R2.evaluate([c1[i], c2[j]])
        
X, Y = np.meshgrid(c1, c2)
fig.add_trace(
    go.Surface(x=X, y=Y, z=Z1, colorscale='Viridis', showscale=False),
    row=1, col=1)

fig.add_trace(
    go.Surface(x=X, y=Y, z=Z2, colorscale='Viridis', showscale=False),
    row=1, col=2)


c1 = np.linspace(1.480001,2.5,nd)
c2 = np.linspace(10,20,nd)

Z1 = np.zeros((nd,nd))
Z2 = np.zeros((nd,nd))
for i in range(nd):
    for j in range(nd):
        Z1[j,i] = R1.evaluate([c1[i], c2[j]])
        Z2[j,i] = R2.evaluate([c1[i], c2[j]])
        

fig.add_trace(
    go.Surface(x=X, y=Y, z=Z1, colorscale='Viridis', showscale=False),
    row=2, col=1)

fig.add_trace(
    go.Surface(x=X, y=Y, z=Z2, colorscale='Viridis', showscale=False),
    row=2, col=2)

c1 = np.linspace(0.5,2.5,nd)
c2 = np.linspace(10,20,nd)

Z1 = np.zeros((nd,nd))
Z2 = np.zeros((nd,nd))
for i in range(nd):
    for j in range(nd):
        Z1[j,i] = R1.evaluate([c1[i], c2[j]])
        Z2[j,i] = R2.evaluate([c1[i], c2[j]])
        

fig.add_trace(
    go.Surface(x=X, y=Y, z=Z1, colorscale='Viridis', showscale=False),
    row=3, col=1)

fig.add_trace(
    go.Surface(x=X, y=Y, z=Z2, colorscale='Viridis', showscale=False),
    row=3, col=2)


pplot(fig)