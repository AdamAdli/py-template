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

# Non-standard Imports
import numpy as np
import pandas as pd  # Prefer aliasing to maintain clarity and convention

########################################################################################################################
# Globals & Constants
########################################################################################################################

__author__ = "Adam Adli (adam@adli.ca)"
__description__ = "Python script template."
__file_dir__ = os.path.dirname(os.path.abspath(__file__))
__exec_time__ = datetime.datetime.now()
logger = logging.getLogger(name=__name__)


########################################################################################################################
# Script: init() - declaring arguments
########################################################################################################################

def init(parser: argparse.ArgumentParser = None) -> argparse.ArgumentParser:
    """
    Initializes and returns the argument parser with script-specific options.

    :param argparse.ArgumentParser parser: An existing argument parser instance to be extended with script-specific arguments. If None, a new argument parser instance will be created.
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


def generate_random_dataframe(rows: int = 5, cols: int = 5) -> pd.DataFrame:
    """
    Generates a random pandas DataFrame.

    :param int rows: Number of rows in the DataFrame. Defaults to 5.
    :param int cols: Number of columns in the DataFrame. Defaults to 5.
    :return: A pandas DataFrame containing random numbers.
    :rtype: pd.DataFrame
    """
    data = np.random.rand(rows, cols)  # Generate a 2D numpy array of random floats
    dataframe = pd.DataFrame(data, columns=[f'Column{i + 1}' for i in range(cols)])
    return dataframe


def log_dataframe(df: pd.DataFrame) -> None:
    """
    Logs the contents of a pandas DataFrame as a string.

    :param pd.DataFrame df: The DataFrame to log.
    """
    # Convert the DataFrame to a string and log it
    df_string = df.to_string()
    logger.info(f"DataFrame contents:\n{df_string}")


########################################################################################################################
# Main
########################################################################################################################

def main(args: argparse.Namespace) -> int:
    """
    Main function of the script.

    :param argparse.Namespace args: The namespace containing the script arguments.
    :return: An integer to be used as the script's exit code. 0 indicates success.
    :rtype: int
    """
    logger.info("Hello world.")

    # Example usage of script body functions.

    # Generate a random DataFrame
    random_df = generate_random_dataframe()

    # Log the DataFrame contents
    log_dataframe(random_df)

    return 0  # Return 0 for success.


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s[%(name)s.%(funcName)s]: %(message)s",
                        handlers=[logging.StreamHandler(stream=sys.stdout)])
    logging.info(f"Starting {__file__}")
    pythonpath = os.environ.get('PYTHONPATH', '')
    logging.info(f"PYTHONPATH=\"{pythonpath}\"")
    logging.info(f"{sys.executable} {' '.join(sys.argv)}")

    main_parser = init()  # Initialize the argument parser
    main_args = main_parser.parse_args()  # Parse the actual arguments passed to this script

    if main_args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    exit_code = main(main_args)  # Call main function and get the exit code
    sys.exit(exit_code)
