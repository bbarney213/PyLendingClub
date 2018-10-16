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

.. |commits-since| image:: https://img.shields.io/github/commits-since/bbarney213/PyLendingClub/v3.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/bbarney213/PyLendingClub/compare/v3.0.1...master

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

* Free software: BSD 3-Clause License

Installation
============

::

    pip install pylendingclub
    
About
============

A Python based wrapper for Lending Club's API that enables easier programmatic use of the API. Also extends the functionality of the API through a higher-level wrapper for ease of use, and an AutoInvestor. More features to come.

See the API documentation here: https://www.lendingclub.com/developers/api-overview.

Getting Started
============

To get started, download the package with pip:

::

    pip install pylendingclub


Once the package is installed, you will need a Session object. You can create one directly, by passing your api-key_ and investor-id_.
    
    .. _api-key: https://www.lendingclub.com/account/profile.action
    .. _investor-id: https://www.lendingclub.com/account/summary.action

::

    from pylendingclub.session import LendingClubSession
    session = LendingClubSession(api_key, investor_id)
    
    
    

Alternatively, you can create environment variables for both of these values. Make sure they are created as 'LC_API_KEY' and 'LC_INVESTOR_ID'.

With environment variables set, you can create a `Session` with them like so:

::

    from pylendingclub import Session
    session = LendingClubSession.from_environment_variables()


Using the Session Object
============

Sessions and Responses
============
Calls to the API through the `Session` will return a Response_ object. You can then work with this response as needed. If you just want the JSON data from the response, use the following syntax:

    .. _Response : http://docs.python-requests.org/en/master/api/#requests.Response

::

    response = session.resource.property
    json_data = response.json()


or

::

    response = session.resource.method()
    json_data = response.json()

You can also chain the `.json()` call directly onto the property, or method, but this won't allow you to handle an error with the response without making a separate call to get the original response. Especially when working with the `POST` methods, it is recommended to store the response separate from the JSON, but it is not required.

Accessing Resources
============
There are two primary resources available within the API. These are the `Account` and `Loan` resources. You can access them within the `Session` like so:

::

    account = session.account
    loan = session.loan


These two resources expose the sub-resources/services within the API. More on this below.

**Remember, all of these services will return a `Response`.**

Account Resource
============

Account Summary
============

API Documentation: https://www.lendingclub.com/developers/summary

Method Type: GET

Syntax:
::

    account_summary = session.account.summary
    
    
Available Cash
============

API Documentation: https://www.lendingclub.com/developers/available-cash

Method Type: GET

Syntax:
::

    available_cash = session.account.available_cash

Notes
============

API Documentation: https://www.lendingclub.com/developers/notes-owned

Method Type: GET

Syntax:
::

    notes = session.account.notes

Detailed Notes
============

API Documentation: https://www.lendingclub.com/developers/detailed-notes-owned

Method Type: GET

Syntax:
::

    detailed_notes = session.account.detailed_notes

Portfolios Owned
============

API Documentation: https://www.lendingclub.com/developers/portfolios-owned

Method Type: GET

Syntax:
::

    portfolios_owned = session.account.portfolios_owned

Filters
============

API Documentation: https://www.lendingclub.com/developers/filters

Method Type: GET

Syntax:
::

    filters = session.account.filters

Create Portfolio
============

API Documentation: https://www.lendingclub.com/developers/create-portfolio

Method Type: POST

Syntax:
::

    create_portfolio = session.account.create_portfolio(portfolio_name, [portfolio_description])

Submit Orders
============

API Documentation: https://www.lendingclub.com/developers/submit-order

Note:

The orders must be a list of dicts in the format:
::

    [
      {
        'loanId' : loan_id,
        'requestedAmount' : amount,
        'portfolioId' : portfolio_id
      }
    ]

Where `loanId` and `requestedAmount` are required, and `requestedAmount` must be a denomination of 25.

For example:

::

    [
      {
        'loanId' : 1234,
        'requestedAmount' : 25,
      },
      {
        'loanId' : 1345,
        'requestedAmount' : 50,
        'portfolioId' : 12345
      }
    ]

Method Type: POST

Syntax:
::

    submit_orders = session.account.submit_orders(orders)

Submit Order
============

API Documentation: https://www.lendingclub.com/developers/submit-order

Method Type: POST

Note: The `requested_amount` must be a denomination of $25.00. For example, 25, 100, and 2000 are all accepted values but 26, 115, and 2010 are not.

Syntax:
::

    submit_order = session.account.submit_order(loan_id, requested_amount, [portfolio_id])

Account/Funds
============

Pending Transfers
============

API Documentation: https://www.lendingclub.com/developers/pending-transfers

Method Type: GET

Syntax:
::

    pending_transfers = session.account.funds.pending

Add
============

API Documentation: https://www.lendingclub.com/developers/add-funds

Method Type: POST

Notes:

The `transfer_frequency` argument must be one of `[LOAD_NOW, LOAD_ONCE, LOAD_WEEKLY, LOAD_BIWEEKLY, LOAD_ON_DAY_1_AND_16, LOAD_MONTHLY]`

The 'start_date' argument is required for recurring transfers, and for `LOAD_ONCE`.

Syntax:
::

    add_funds = session.account.funds.add(amount, transfer_frequency, [start_date], [end_date])

Withdraw
============

API Documentation: https://www.lendingclub.com/developers/add-funds

Method Type: POST

Syntax:
::

    withdraw_funds = session.account.funds.withdraw(amount)

Cancel Transfer
============

API Documentation: https://www.lendingclub.com/developers/cancel-transfers

Method Type: POST

Syntax:
::

    cancel_transfer = session.account.funds.cancel(transfer_id)

Loan Resource
============

Listed Loans
============

API Documentation: https://www.lendingclub.com/developers/listed-loans

Method Type: GET

Notes: 

The `show_all` argument will determine whether all loans are shown, or only the loans from the most recent listing period are shown.

The `filter_id` argument, if provided, will only show loans matching the filter.

Syntax:
::

    listed_loans = session.loan.listed_loans([filter_id], [show_all]=True)
