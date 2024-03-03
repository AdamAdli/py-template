"""
    Python script template to help you structure your python code.
    Author: Adam Adli, 2024.
"""
########################################################################################################################
# Imports
########################################################################################################################

# Standard Imports
from __future__ import annotations

import argparse
import datetime
import logging
import os
import sys
from typing import Optional


# Non-standard Imports
import matplotlib.pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pandas.api.types import infer_dtype
from pandas.api.types import is_numeric_dtype, is_string_dtype

########################################################################################################################
# Globals & Constants
########################################################################################################################

__author__ = "Adam Adli (adam@adli.ca)"
__description__ = "Python script template."

# Directory where this script is located.
__file_dir__ = os.path.dirname(os.path.abspath(__file__))

# Timestamp this script was executed.
__exec_time__ = datetime.datetime.now()

# Logger for this module.
logger = logging.getLogger(name=__name__)


########################################################################################################################
# Script: init()
########################################################################################################################

def init(parser: Optional[argparse.ArgumentParser] = None) -> argparse.ArgumentParser:
    """
    Initializes and returns the argument parser with script-specific options.

    :param Optional[argparse.ArgumentParser] parser: An existing argument parser instance to be extended with script-specific arguments. If None, a new argument parser instance will be created.
    :return: The initialized argument parser.
    :rtype: argparse.ArgumentParser
    """
    parser = parser or argparse.ArgumentParser(description=__description__, conflict_handler='resolve')
    parser.add_argument('--debug', dest='debug', action='store_true', default=False,
                        help="Enables debugging functionality.")
    return parser


########################################################################################################################
# Script: Body
########################################################################################################################


def infer_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Infers and returns the types of columns in the given DataFrame.

    :param pd.DataFrame df: DataFrame for which the column types need to be inferred.
    :return: A new DataFrame with the original column names and their inferred types.
    :rtype: pd.DataFrame
    """
    inferred_types = {}
    for column in df.columns:
        if is_numeric_dtype(df[column]):
            inferred_types[column] = 'Numeric'
        elif is_string_dtype(df[column]):
            inferred_types[column] = 'String'
        else:
            inferred_types[column] = 'Object'
    return pd.DataFrame(list(inferred_types.items()), columns=['Column', 'Inferred Type'])


def apply_inferred_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies inferred types to the columns of the given DataFrame.

    :param pd.DataFrame df: DataFrame for which the column types need to be inferred and applied.
    :return: The DataFrame with applied column types.
    :rtype: pd.DataFrame
    """
    for column in df.columns:
        try:
            inferred_type = infer_dtype(df[column])
            if inferred_type == 'integer':
                df[column] = pd.to_numeric(df[column], downcast='integer')
            elif inferred_type == 'floating':
                df[column] = pd.to_numeric(df[column], downcast='float')
            elif inferred_type == 'string':
                df[column] = df[column].astype(str)
        except Exception as e:
            logger.error(f"Could not convert column {column}. Error: {e}")
    return df


def plot_world_population(df: pd.DataFrame) -> None:
    """
    Plots the world population over the years from the given DataFrame.

    :param pd.DataFrame df: DataFrame containing the world demographic data.
    """
    df['Year'] = pd.to_datetime(df['Year'].astype(str))
    df['World Population (in millions)'] = df['World Population (in thousands)'] / 1000
    plt.figure(figsize=(12, 6))
    plt.plot(df['Year'], df['World Population (in millions)'], marker='o')
    plt.title('World Population Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Population (in millions)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def scrape_wikipedia_demographics(url: str) -> Optional[pd.DataFrame]:
    """
    Scrapes the historical vital statistics table from a specified Wikipedia page.

    :param str url: URL of the Wikipedia page to scrape.
    :return: A pandas DataFrame containing the scraped data, or None if an error occurs.
    :rtype: Optional[pd.DataFrame]
    """
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table', {'class': 'wikitable'})
        if table:
            return pd.read_html(str(table))[0]
    except Exception as e:
        logger.error(f"An error occurred while scraping: {e}")
    return None


########################################################################################################################
# Script: Main
########################################################################################################################


def main(args: argparse.Namespace) -> int:
    """
    Main function of the script.

    :param argparse.Namespace args: The namespace containing the script arguments.
    :return: An integer to be used as the script's exit code.
    :rtype: int
    """
    logger.info("Starting script.")
    url = "https://en.wikipedia.org/wiki/Demographics_of_the_world"
    df = scrape_wikipedia_demographics(url)
    if df is not None:
        df = apply_inferred_types(df)
        plot_world_population(df)
        logger.info("Demographics DataFrame:\n%s", df.to_string())
    return 0  # Return 0 for success


# Main Guard: only runs this code if this script is run directly and not used as an import in another script.
# Initialize logger, parse arguments, and calls main function().
if __name__ == '__main__':

    # Setup logger - see: https://docs.python.org/3/howto/logging.html
    logging.basicConfig(
        # Try changing level to see what happens?
        level=logging.INFO,

        # Formats the log message output.
        format="%(asctime)s - %(levelname)s[%(name)s.%(funcName)s]: %(message)s",

        handlers=[
            # Uncommenting the filehandler will create a log file, make the logger also
            # write all log messages to <script_name>.log.
            # logging.FileHandler(filename=f'{__file__}.log', mode='w'),

            # Prints log messages to your terminal output.
            logging.StreamHandler(stream=sys.stdout)
        ]
    )

    # Let's log some messages showinbg how this script was executed.
    logging.info(f"Starting {__file__}")
    logging.info(f"PYTHONPATH=\"{os.environ['PYTHONPATH'] if 'PYTHONPATH' in os.environ else ''}\"")
    logging.info(f"{sys.executable} {' '.join(sys.argv)}")

    # Call init() function that sets up the argument parser.
    main_parser = init(argparse.ArgumentParser(description=__description__, conflict_handler='resolve'))

    # Parse the actual arguments passed to this script.
    main_args = main_parser.parse_args()

    if main_args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    # Call main(args)
    main_rc = main(main_args)

    # Exit python with the return code we got from main().
    exit(main_rc)
