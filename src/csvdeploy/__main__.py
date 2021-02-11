#!/usr/bin/env python3

"""
__main__.py

Module for command-line execution of alignment.
"""

# Import Python standard libraries
import argparse
import logging

# Import our library
import csvdeploy


def parse_arguments():
    """
    Parses arguments and returns them in a namespace.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("configfile", type=str, help="Path to the configuration file.")
    args = parser.parse_args()

    return args


def main():
    """
    Entry point for the command-line tool.
    """

    # Parse command-line arguments
    args = parse_arguments()

    # Read and parse configuration file
    config, replaces = csvdeploy.load_config(args.configfile)

    # Read the data
    # TODO: fix for multiple tables and metadata
    data = {}
    data["single"] = csvdeploy.read_data(config)

    config["single_table"] = [
        "GLOTTOCODE",
        "NAME",
        "ISO_CODE",
        "LATITUDE",
        "LONGITUDE",
        "GLOTTOLOG_FAMILY",
        "TRESOLDI_GENUS",
    ]
    # Build site
    csvdeploy.render_site(data, replaces, config)


if __name__ == "__main__":
    # TODO: allow to override logging level
    logging.basicConfig(level=logging.INFO)
    main()
