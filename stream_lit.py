import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

freq = st.slider('Frequency', 0.1, 40.0, 1.0)
color_high = st.color_picker('high color', '#0000FF')
color_low = st.color_picker('low color', '#FF0000')

# Define the function
def f(x, y):
    return 4 * x**2 + y**2 + 1

# Create a grid of x and y values
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Create a custom colormap
cmap = LinearSegmentedColormap.from_list('custom_cmap', [color_low, color_high])

# Create the contour plot
fig, ax = plt.subplots()
contour = ax.contour(X, Y, Z, levels=50, cmap=cmap)
ax.set_title('Contour map of f(x, y) = 4x^2 + y^2 + 1')
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.colorbar(contour)

# Add x and y axes
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)

# Display the plot using Streamlit
st.pyplot(fig)