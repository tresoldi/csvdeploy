# Import Python standard libraries
import json
import logging
import csv
from pathlib import Path

# Import 3rd party libraries
from jinja2 import Environment, FileSystemLoader
import markdown


def read_plain_csv(filename: str, delimiter: str = ",", encoding: str = "utf-8"):
    """
    Read a plain CSV file, without metadata.

    The function works mostly as a wrapper to the standard library.
    """

    with open(filename, encoding=encoding) as handler:
        data = list(csv.DictReader(handler, delimiter=delimiter))

    return data


# Inner function for loading markdown files and converting them to HTML
# TODO: only convert if .md
def _md2html(filename, base_path):
    logging.info("Reading contents from `%s`..." % filename)
    content_path = base_path / "contents" / filename
    with open(content_path.as_posix()) as handler:
        source = markdown.markdown(handler.read())

    return source


# TODO: merge `config` and `replaces` into a single dict?
def load_config(base_path: str):
    """
    Load configuration, contents, and replacements.

    The function will load configuration from a single JSON config file,
    returning a dictionary of configurations and a dictionary of
    replacements that includes markdown contents read from files.

    Parameters
    ----------
    base_path : pathlib.Path
        Base path of the deployment system.
    Returns
    -------
    config : dict
        A dictionary of dataset and webpage configurations.
    replaces : dict
        A dictionary of replacements, for filling templates.
    """

    # Use `pathlib` for (hopefully) system-agnostic paths and for facilitating
    # operations
    base_path = Path(base_path)

    # Load JSON data
    # TODO: add a "config.json" if the path does not end in a file
    logging.info("Loading JSON configuration...")
    with open(base_path) as config_file:
        config = json.load(config_file)

    config["base_path"] = base_path.parent

    # Build replacement dictionary; which for future expansions it is
    # preferable to keep separate from the actual configuration while
    # using a single file not to scare potential users with too much
    # structure to learn. Remember that, in order to make
    # deployment easy, we are being quite strict here in terms of
    # templates, etc.
    replaces = {
        "title": config["title"],
        "description": config["description"],
        "author": config["author"],
        "favicon": config["favicon"],
        "mainlink": config["mainlink"],  # TODO: should be derived from URL?
        "citation": config["citation"],
    }

    return config, replaces


def load_template_env(config):
    logging.info("Loading templates...")

    # Build template_file and layout path; note that
    # Jinja2 documentation says that template names are not filesystem paths (even though
    # they map to filesystem paths), so that forward slashes should always be used,
    # even under Windows.
    # TODO: makes sure this works out of the box all the time
    if "template_path" in config:
        template_path = Path(config["template_path"])
    else:
        template_path = Path(__file__).parent.parent.parent / "template_html"
    template_path = template_path.as_posix().replace("\\", "/")

    template_env = Environment(loader=FileSystemLoader(template_path))

    return template_env


def read_pure_data(config):
    source_file = config["base_path"] / config["source"]
    data = read_plain_csv(source_file, delimiter="\t")

    return data

def read_csvw_data(config):
    pass
