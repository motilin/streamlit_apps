# Contour Plot Streamlit App

This Streamlit app generates a contour plot based on user-defined parameters. The app allows users to adjust the spacing between contour lines, as well as other parameters, and it enables easy saving of the plot.

## Installation

### Using pip

1. **Clone the repository:**
   ```sh
   git clone https://github.com/motilin/streamlit_apps.git
   cd streamlit_apps
   ```

2. **Create a virtual environment (optional but recommended):**
   ```sh
   python3 -m venv streamlit
   source streamlit/bin/activate  # On Windows use `streamlit\Scripts\activate`
   ```

3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

### Using conda

1. **Clone the repository:**
   ```sh
   git clone https://github.com/motilin/streamlit_apps.git
   cd streamlit_apps
   ```

2. **Create a conda environment:**
   ```sh
   conda create --name streamlit python=3.9
   conda activate streamlit
   ```

3. **Install the required packages:**
   ```sh
   conda install --file requirements.txt
   ```

## Running the App

To run the Streamlit app, use the following command:
```sh
streamlit run contour_plot.py
```

This will start the Streamlit server and open the app in your default web browser.

## Usage

- Adjust the sliders and color pickers in the sidebar to customize the contour plot.
- Click the "Save Plot" button in the sidebar to save the plot as a PNG, PDF, or SVG file.

## Requirements

- Python 3.9 or higher
- `matplotlib==3.9.2`
- `numpy==2.1.3`
- `streamlit==1.25.0`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.