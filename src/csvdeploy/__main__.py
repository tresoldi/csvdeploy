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

    # If the `config` does not specify the columns to use, use all of them
    # TODO: move this logic to configuration reading/parsing
    if "single_table" not in config:
        config["single_table"] = list(data["single"][0].keys())

    # Build list of table replaces (for header, mostly)
    table_names = [key for key in config if key.endswith("_table")]
    tables = []
    for tname in table_names:
        label = tname.split("_")[0]
        tables.append({"name": label.capitalize(), "url": f"{label}.html"})

    # Build site
    csvdeploy.render_site(data, replaces, tables, config)


if __name__ == "__main__":
    # TODO: allow to override logging level
    logging.basicConfig(level=logging.INFO)
    main()
