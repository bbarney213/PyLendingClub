import requests

from .session import LendingClubSession
from ..config.config import LC_API_VERSION

def test_api_key():
    return os.environ(['LC_API_KEY'])

def test_investor_id():
    return os.environ(['LC_INVESTOR_ID'])

def test_account_summary_keys():
    return [
        'investorId', 'availableCash', 'accountTotal',
        'accruedInterest', 'infundingBalance', 'receivedInterest',
        'receivedPrincipal', 'receivedLateFees', 'outstandingPrincipal',
        'totalNotes', 'totalPortfolios', 'netAnnualizedReturn',
        'adjustments'
    ]

def test_available_cash_keys():
    return [
        'investorId', 'availableCash'
    ]

def test_notes_keys():
    return [
        'myNotes'
    ]

def test_detailed_notes_keys():
    return [
        'myNotes'
    ]

def test_portfolios_owned_keys():
    return [
        'myPortfolios'
    ]

def test_filters_keys():
    return [

    ]

def test_funds_pending_keys():
    return [

    ]

def test_listed_loans_keys():
    return [
        'asOfDate', 'loans'
    ]

def test_session():
    return LendingClubSession(test_api_version(), test_api_key(), test_investor_id())


def is_response(value):
    return isinstance(value, requests.Response)

def is_successful_response(value):
    return value.status_code == 200

def test_response(response, keys):
    assert is_response(response), 'Response provided is not a Response object.'
    assert is_successful_response(response), 'Response from the API was not successful. Status Code {}: {}'.format(response.status_code, response.reason)
    assert isinstance(response.json(), dict), 'Unable to get JSON from response.'
    assert set(keys).issubset(response.json().keys()), 'Response JSON missing expected fields.'



def run_lc_tests():
    session = test_session()

    test_response(session.account.summary, test_account_summary_keys())
    test_response(session.account.available_cash, test_available_cash_keys())
    test_response(session.account.notes, test_notes_keys())
    test_response(session.account.detailed_notes, test_detailed_notes_keys())
    test_response(session.account.portfolios_owned, test_portfolios_owned_keys())
    test_response(session.account.filters, test_filters_keys())
    test_response(session.account.funds.pending, test_funds_pending_keys())
    test_response(session.loan.listed_loans(), test_listed_loans_keys())

    print('All tests passed.')

if __name__ == '__main__':
    run_lc_tests()
