import requests

from pylendingclub.config import LC_API_VERSION
from pylendingclub.wrapper.session import LendingClubSession

def account_summary_keys():
    return [
        'investorId', 'availableCash', 'accountTotal',
        'accruedInterest', 'infundingBalance', 'receivedInterest',
        'receivedPrincipal', 'receivedLateFees', 'outstandingPrincipal',
        'totalNotes', 'totalPortfolios', 'netAnnualizedReturn',
        'adjustments'
    ]

def available_cash_keys():
    return [
        'investorId', 'availableCash'
    ]

def notes_keys():
    return [
        'myNotes'
    ]

def detailed_notes_keys():
    return [
        'myNotes'
    ]

def portfolios_owned_keys():
    return [
        'myPortfolios'
    ]

def filters_keys():
    return [

    ]

def funds_pending_keys():
    return [

    ]

def listed_loans_keys():
    return [
        'asOfDate', 'loans'
    ]

def is_response(value):
    return isinstance(value, requests.Response)

def is_successful_response(value):
    return value.status_code == 200

def check_response(response, keys):
    assert is_response(response), 'Response provided is not a Response object.'
    assert is_successful_response(response), 'Response from the API was not successful. Status Code {}: {}'.format(response.status_code, response.reason)
    assert isinstance(response.json(), dict), 'Unable to get JSON from response.'
    assert set(keys).issubset(response.json().keys()), 'Response JSON missing expected fields.'



def test_wrapper():
    session = LendingClubSession.from_environment_variables()

    check_response(session.account.summary, account_summary_keys())
    check_response(session.account.available_cash, available_cash_keys())
    check_response(session.account.notes, notes_keys())
    check_response(session.account.detailed_notes, detailed_notes_keys())
    check_response(session.account.portfolios_owned, portfolios_owned_keys())
    check_response(session.account.filters, filters_keys())
    check_response(session.account.funds.pending, funds_pending_keys())
    check_response(session.loan.listed_loans(), listed_loans_keys())

    print('All tests passed.')

if __name__ == '__main__':
    test_wrapper()
