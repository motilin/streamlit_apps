import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import os

# Set page configuration
st.set_page_config(layout="centered")


# Main Streamlit app
def main():
    # Create the plot
    fig = create_plot()

    # Display the plot
    st.pyplot(fig)

    # Save button and file naming in sidebar
    st.sidebar.header("Save Plot")

    # File naming with save location
    save_filename = st.sidebar.text_input("Enter filename:", value="plot.png")

    if st.sidebar.button("Save Plot"):
        # Check file extension
        _, file_extension = os.path.splitext(save_filename)

        if file_extension.lower():
            try:
                # Save the figure
                fig.savefig(save_filename)
                st.sidebar.success(f"Plot saved successfully as {save_filename}")
            except Exception as e:
                st.sidebar.error(f"Error saving plot: {e}")
        else:
            st.sidebar.error("Please enter a valid filename")


# Sidebar for controls
st.sidebar.title("Plot Controls")

# Sliders and color pickers
k_spacing = st.sidebar.slider("k_spacing", 0.1, 0.5, step=0.01, value=0.2)
line_width = st.sidebar.slider("line width", 0.1, 2.0, 0.5)
color_high = st.sidebar.color_picker("high color", "#0000FF")
color_low = st.sidebar.color_picker("low color", "#FF0000")


# Define the function
def f(x, y):
    return -3 * y / (x**2 + y**2 + 1)


# Create a grid of x and y values
x = np.linspace(-10, 10, 300)
y = np.linspace(-10, 10, 300)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Create a custom colormap
cmap = LinearSegmentedColormap.from_list("custom_cmap", [color_low, color_high])

# Calculate contour levels based on k_spacing
z_min, z_max = Z.min(), Z.max()
levels = np.arange(z_min, z_max, k_spacing)


# Create the plot function to reuse for display and saving
def create_plot():
    fig, ax = plt.subplots(figsize=(10, 8))
    contour = ax.contour(X, Y, Z, levels=levels, cmap=cmap, linewidths=line_width)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Contour Plot of f(x,y)")
    fig.colorbar(contour)

    # Add x and y axes
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)

    return fig


# Run the app
if __name__ == "__main__":
    main()