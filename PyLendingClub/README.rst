========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/PyLendingClub/badge/?style=flat
    :target: https://readthedocs.org/projects/PyLendingClub
    :alt: Documentation Status


.. |travis| image:: https://travis-ci.org/bbarney213/PyLendingClub.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/bbarney213/PyLendingClub

.. |codecov| image:: https://codecov.io/github/bbarney213/PyLendingClub/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/bbarney213/PyLendingClub

.. |version| image:: https://img.shields.io/pypi/v/pylendingclub.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pylendingclub

.. |commits-since| image:: https://img.shields.io/github/commits-since/bbarney213/PyLendingClub/v4.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/bbarney213/PyLendingClub/compare/v4.0.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/pylendingclub.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/pylendingclub

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pylendingclub.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pylendingclub

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pylendingclub.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/pylendingclub


.. end-badges

An example package. Generated with cookiecutter-pylibrary.

* Free software: BSD 3-Clause License

Installation
============

::

    pip install pylendingclub

Documentation
=============


https://PyLendingClub.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
