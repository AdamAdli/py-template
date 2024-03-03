# Python Script Template Project

This project contains Python script templates to help structure Python code for data scraping and analysis. It includes examples of web scraping, data processing, and data visualization.

## Prerequisites

Before you start, make sure you have the following installed:

- **Git**: Used for version control and to clone the project repository. Download and install from [Git - Downloads](https://git-scm.com/downloads).
- **Python 3.11**: The programming language used for this project. Download and install from [Python Downloads](https://www.python.org/downloads/).
- **PyCharm Community Edition**: An Integrated Development Environment (IDE) for Python. Download and install from [JetBrains: PyCharm](https://www.jetbrains.com/pycharm/download/). You can upgrade to PyCharm Professional for free with a university email to access more features.

## Getting Started

1. **Clone the Repository**: Open PyCharm, go to `File > New > Project from Version Control` and enter the repository URL `https://github.com/AdamAdli/py-template`. PyCharm will automatically clone the repository for you.

2. **Set up a Virtual Environment**:
    - In PyCharm, navigate to `File > Settings > Project: py-template > Python Interpreter`.
    - Click on the settings wheel, choose `Add`, and select `Virtual Environment`.
    - Make sure the `Base interpreter` is set to Python 3.11 and click `OK`.
    - PyCharm will create and activate a new virtual environment for the project.

3. **Install Dependencies**:
    - Open the Terminal in PyCharm (usually at the bottom of the IDE).
    - Run the following command to install the project's dependencies:
      ```bash
      pip install -r requirements.txt
      ```

## Running the Scripts

1. **Open the Script**: In PyCharm, navigate to the `example_wiki_scraper.py` or `script_template.py` file in the Project Explorer.

2. **Run the Script**: Right-click on the open script file and select `Run 'script_template'` to execute the script. You can also use the green play button in the top-right corner.

3. **View Output**: The output will be displayed in the Run window at the bottom of PyCharm.

## Project Structure

- `.idea/`: PyCharm project settings.
- `.venv/`: Virtual environment files.
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `example_wiki_scraper.py`: An example script for web scraping and data processing.
- `script_template.py`: A template for Python scripting.
- `README.md`: This file, containing project documentation.
- `requirements.txt`: The list of packages required to run the scripts.

## Contributing

Feel free to fork the repository, make changes, and submit pull requests. If you find any issues or have suggestions for improvements, please open an issue in the GitHub repository.

## License

This project is open-sourced under the [MIT License](https://opensource.org/licenses/MIT).

