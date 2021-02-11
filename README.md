# csvdeploy

Python package for deploying tabular data files (csvw) as static websites with continuous integration

## Introduction

`csvdeploy` is a Python library for the generation and deployment of static websites
based on tabular data following [csvw](the https://www.w3.org/TR/tabular-data-primer/) standard
from W3C. It intended as a solution for simple websites requiring almost no configuration and
which can be served on cheap or free hosting services: out goal is to have a tool that is
as "plug-and-play" as possible, and which can be configured for continuous integration.

## Installation and usage

The library can be installed as any standard Python library with `pip`, as in the snippet
below. If installed in a local machine, it is highly recommended using a virtual
environment solution. In all cases, updating the packages used for installing libraries
is also recommended whenever possible (that is, `pip install --upgrade pip setuptools wheel`).

```bash
$ pip install deploycsv
```

In most situations, however, you will probably want to use the library automatically in
some integrated system. The intended usage is to have a `git` repository holding
your data that will automatically invoke `csvdeploy`, generate the new web pages, and
upload them to be served each time the raw data is changed. The instructions for
installing and using the library will depend on the exact system you will be using,
with the most common given in our documentation.

## Changelog

Version 0.1:

  - First released version.

## Community guidelines

While the author can be contacted directly for support, it is recommended that third parties use
GitHub standard features, such as issues and pull requests, to contribute, report problems, or
seek support.

Contributing guidelines, including a code of conduct, can be found in the `CONTRIBUTING.md` file.

## Author and citation

The library is developed by Tiago Tresoldi (tiago.tresoldi@lingfil.uu.se).

During initial stage of development, the author received funding from the European Research Council
(ERC) under the European Union's Horizon 2020 research and innovation programme (grant agreement No.
ERC Grant #715618, "Computer-Assisted Language Comparison").

If you use `csvdeploy`, please cite it as:

  > Tresoldi, Tiago (2021). CSVDeploy, a package for deploying tabular data files as static websites.
  > Version 0.1. Uppsala.

In BibTeX:

```
@misc{Tresoldi2021csvdeploy,
  author = {Tresoldi, Tiago},
  title = {CSVDeploy, a package for deploying tabular data files as static websites. Version 0.1},
  howpublished = {\url{https://github.com/tresoldi/csvdeploy}},
  address = {Uppsala},
  publisher = {Institutionen för lingvistik och filologi, Uppsala universitet}
  year = {2021},
}
```