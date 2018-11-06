if __name__ == '__main__':
    import sys
    from os.path import dirname, abspath, join
    package_path = join(dirname(dirname(dirname(abspath(__file__)))), 'src')
    sys.path.insert(0, package_path)

import requests

from pylendingclub.wrapper.session import LendingClubSession

ACCOUNT_SUMMARY_KEYS = ['investorId', 'availableCash', 'accountTotal',
    'accruedInterest', 'infundingBalance', 'receivedInterest',
    'receivedPrincipal', 'receivedLateFees', 'outstandingPrincipal',
    'totalNotes', 'totalPortfolios', 'netAnnualizedReturn',
    'adjustments']
AVAILABLE_CASH_KEYS = ['investorId', 'availableCash']
NOTES_KEYS = DETAILED_NOTES_KEYS = ['myNotes']
PORTFOLIOS_OWNED_KEYS = ['myPortfolios']
FILTERS_KEYS = []
FUNDS_PENDING_KEYS = []
LISTED_LOANS_KEYS = ['asOfDate', 'loans']

def check_response(response, keys, name):
    try:
        assert isinstance(response, requests.Response), 'Response provided is not a Response object.'
        assert response.status_code == 200, 'Response from the API was not successful. Status Code {}: {}'.format(
            response.status_code, response.reason)
        assert isinstance(response.json(), dict), 'Unable to get JSON from response.'
        if len(response.json()) > 0:
            assert set(keys).issubset(response.json().keys()), 'Response JSON missing expected fields.'
        else:
            print('Unable to check the response keys for the {} resource. Response is empty.'.format(name))
    except AssertionError as e:
        print('Tests Failed:')
        print('Method: {}'.format(name))
        print('Response:', response)
        try:
            print('Response JSON:', response.json())
        except AttributeError as e:
            pass
        raise

def test_wrapper():
    session = LendingClubSession.from_environment_variables(True)
    check_response(session.account.summary, ACCOUNT_SUMMARY_KEYS, 'Account Summary')
    check_response(session.account.available_cash, AVAILABLE_CASH_KEYS, 'Available Cash')
    check_response(session.account.notes, NOTES_KEYS, 'Notes')
    check_response(session.account.detailed_notes, DETAILED_NOTES_KEYS, 'Detailed Notes')
    check_response(session.account.portfolios_owned, PORTFOLIOS_OWNED_KEYS, 'Portfolios Owned')
    check_response(session.account.filters, FILTERS_KEYS, 'Filters')
    check_response(session.account.funds.pending, FUNDS_PENDING_KEYS, 'Funds Pending')
    check_response(session.loan.listed_loans(), LISTED_LOANS_KEYS, 'Listed Loans')
    print('All tests passed.')


if __name__ == '__main__':
    test_wrapper()
