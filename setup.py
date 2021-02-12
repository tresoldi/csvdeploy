"""
setup.py script
"""

# Import Python standard libraries
from pathlib import Path
from setuptools import setup, find_packages
import glob

# The directory containing this file
LOCAL_PATH = Path(__file__).parent

# The text of the README file
README_FILE = (LOCAL_PATH / "README.md").read_text()

# Build (recursive) list of resource files
# TODO: read from MANIFEST.in?
resource_files = []
for filename in glob.glob("template_html/*"):
    resource_files.append(filename)

for directory in glob.glob("demo_data/*/"):
    files = glob.glob(directory + "*")
    resource_files.append((directory, files))

# Load requirements, so they are listed in a single place
with open("requirements.txt") as fp:
    install_requires = [dep.strip() for dep in fp.readlines()]

# This call to setup() does all the work
setup(
    author_email="tiago.tresoldi@lingfil.uu.se",
    author="Tiago Tresoldi",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
    ],
    data_files=[("docs", glob.glob("docs/*"))] + resource_files,
    description="A package for deploying tabular data files as static websites",
    entry_points={"console_scripts": ["csvdeploy=csvdeploy.__main__:main"]},
    include_package_data=True,
    install_requires=install_requires,
    keywords=["csv", "tsv", "tabular data", "static website", "deployment"],
    license="GNU GPL3",
    long_description_content_type="text/markdown",
    long_description=README_FILE,
    name="csvdeploy",
    packages=find_packages(where="src"),  # ["csvdeploy", "resources", "docs"],
    package_dir={"": "src"},  # , "resources":"..", "docs":".."},
    #project_urls={"Documentation": "https://malign.readthedocs.io"},
    test_suite="tests",
    tests_require=[],
    url="https://github.com/tresoldi/csvdeploy",
    version="0.1",  # remember to sync with __init__.py
    zip_safe=False,
)
