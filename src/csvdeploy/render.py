import datetime
import logging
from pathlib import Path

from . import common


# TODO: fix navigation bar
# TODO: have a common signature for all functions


def build_tables(data, replaces, tables, template_env, config):
    # TODO: fitting the data to the what is expected by the template
    fields = config["single_table"]

    rows = []
    for row in data["single"]:
        subrow = [{"value": row[field], "url": None} for field in fields]
        rows.append(subrow)

    table_data = {"columns": [{"name": field} for field in fields], "rows": rows}

    for table in data:
        table_replaces = replaces.copy()
        table_replaces["datatable"] = table_data
        build_html(template_env, table_replaces, tables, f"{table}.html", config)


def build_sql_page(data, replaces, template_env, config):
    # Compute inline data replacements
    inline_data = {}
    for table_name in data:
        inline_data[table_name] = []
        for row in data[table_name]["rows"]:
            row_insert = ", ".join(
                ["'%s'" % cell["value"] if cell["value"] else "NULL" for cell in row]
            )
            inline_data[table_name].append(row_insert)

    # Build table schemata
    # TODO: use datatypes
    schemata = {}
    for table_name in data:
        schemata[table_name] = ", ".join(
            ["%s text" % col["name"].lower() for col in data[table_name]["columns"]]
        )

    # Generate page
    sql_replaces = replaces.copy()
    sql_replaces["data"] = inline_data
    sql_replaces["schemata"] = schemata
    build_html(template_env, sql_replaces, "sql.html", config)


# TODO: write properly etc. should load with other templates;
# TODO: also copy images if needed
def build_css(template_env, replaces, config):
    template = template_env.get_template("main.css")

    source = template.render(**replaces)

    # build and writeWrite
    file_path = Path(config["output_path"]) / "main.css"
    with open(file_path.as_posix(), "w") as handler:
        handler.write(source)


def build_html(template_env, replaces, tables, output_file, config):
    """
    Build and write an HTML file from template and replacements.
    """

    # Load proper template and apply replacements, also setting current date
    logging.info("Applying replacements to generate `%s`...", output_file)
    if output_file == "index.html":
        template = template_env.get_template("index.html")
    elif output_file == "sql.html":
        template = template_env.get_template("sql.html")
    else:
        template = template_env.get_template("datatable.html")

    source = template.render(
        tables=tables,
        file=output_file,
        current_time=datetime.datetime.now().ctime(),
        **replaces,
    )

    # Write
    file_path = Path(config["output_path"]) / output_file
    with open(file_path.as_posix(), "w", encoding="utf-8") as handler:
        handler.write(source)

    logging.info("`%s` wrote with %i bytes.", output_file, len(source))


# TODO: have a single argument with replaces, tables, and config
def render_site(data, replaces, tables, config):
    # Load Jinja HTML template environment
    template_env = common.load_template_env(config)

    # Build and write index.html
    build_html(template_env, replaces, tables, "index.html", config)

    # Build CSS files from template
    build_css(template_env, replaces, config)

    # Build tables from CLDF data
    build_tables(data, replaces, tables, template_env, config)

    # Build SQL query page


#    build_sql_page(data, replaces, template_env, config)
