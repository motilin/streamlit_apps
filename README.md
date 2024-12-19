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

## Configuration Instructions for Enabling Live Server Behavior in Streamlit

Streamlit's behavior can be adjusted using a configuration file named `config.toml`. To make Streamlit automatically refresh the app upon saving changes to your script, you need to add the following lines to the `config.toml` file:

```toml
[server]
fileWatcherType = "auto"
runOnSave = true
```

### Location of `config.toml`

The location of the `.streamlit` folder, which contains the `config.toml` file, depends on the operating system:

- **Linux**: The `.streamlit` folder is located in the home directory of the current user. The path is:
  ```
  ~/.streamlit/config.toml
  ```
- **Windows**: The `.streamlit` folder is located in the user's profile directory. The path is:
  ```
  %USERPROFILE%\.streamlit\config.toml
  ```

If the `config.toml` file does not already exist in the `.streamlit` folder, you can create it manually.

### Steps to Enable Live Server Behavior

1. Navigate to the `.streamlit` folder for your operating system.
2. Open or create a `config.toml` file in this directory.
3. Add the following lines to the file:
   ```toml
   [server]
   fileWatcherType = "auto"
   runOnSave = true
   ```
4. Save the file.

Once configured, Streamlit will automatically refresh the app in the browser whenever you save changes to the script, simulating live server behavior.

## Usage

- Adjust the sliders and color pickers in the sidebar to customize the contour plot.
- Click the "Save Plot" button in the sidebar to save the plot as a PNG, PDF, SVG, or any other file format supported by matplotlib.

## Requirements

- Python 3.9 or higher
- `matplotlib==3.9.2`
- `numpy==2.1.3`
- `streamlit==1.25.0`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.