import time

#from pylendingclub.config import LC_INVESTMENT_DENOMINATION
#from pylendingclub.wrapper.base import ExtendedBase
#from pylendingclub.wrapper.funds import Funds
#from pylendingclub.wrapper.resource import Resource

from pylendingclub.config import LC_INVESTMENT_DENOMINATION
from .base import ExtendedBase
from .funds import Funds
from .resource import Resource


class Account(Resource):
    """
    Account resource within the LendingClub API.
    """
    @property
    def summary(self):
        """
        An overall account summary including NAR, available cash, and account balance.

        The GET request for the account/summary resource.

        See: https://www.lendingclub.com/developers/summary
        """
        return self._summary.send()

    @property
    def available_cash(self):
        """
        The available cash within the account..

        The GET request for the account/availablecash resource.

        See: https://www.lendingclub.com/developers/available-cash
        """
        return self._available_cash.send()

    @property
    def notes(self):
        """
        The notes owned by the account.

        The GET request for the account/notes resource.

        See: https://www.lendingclub.com/developers/notes-owned
        """
        return self._notes.send()

    @property
    def detailed_notes(self):
        """
        A detailed list of the notes owned by the account.

        The GET request for the account/detailednotes resource.port

        See: https://www.lendingclub.com/developers/detailed-notes-owned
        """
        return self._detailednotes.send()

    @property
    def portfolios_owned(self):
        """
        All portfolios under the account.

        The GET request for the account/portfolios resource.

        See: https://www.lendingclub.com/developers/portfolios-owned
        """
        return self._portfolios.send()

    @property
    def filters(self):
        """
        All saved filters for the account.

        The GET request for the account/filters resource.

        See: https://www.lendingclub.com/developers/summary
        """
        return self._filters.send()

    def create_portfolio(self, portfolio_name, portfolio_description=None):
        """
        Creates a new portfolio.

        The POST request for the account/portfolios resource.

        See: https://www.lendingclub.com/developers/summary
        """
        payload = {
            'actorId': self._investor_id,
            'portfolioName': portfolio_name
        }

        if portfolio_description:
            payload['portfolioDescription'] = portfolio_description

        return self._create_portfolio.send(payload=payload)

    def submit_orders(self, orders):
        """
        Submits multiple orders in a single batch.

        Takes a list of orders in the form:
        [{ loanId : id,
        requestedAmount : amount,
        portfolioId : portfolioId}, ...]

        Where loanId and requestedAmount are required, and submits the orders
        as a single request.

        The POST request for the account/orders resource.

        See: https://www.lendingclub.com/developers/submit-order
        """
        for order in orders:
            if (order['requestedAmount'] % LC_INVESTMENT_DENOMINATION) != 0:
                raise ValueError('The requested amount must be a denomination of ${:,.2f}. Provided amount for loanId of {} is {}.'
                                 .format(LC_INVESTMENT_DENOMINATION, order['loanId'], order['requestedAmount']))

        payload = {
            'aid': self._investor_id,
            'orders': orders
        }

        return self._submit_orders.send(payload=payload)

    def submit_order(self, loan_id, requested_amount, portfolio_id=None):
        """
        Submits an order for a note, and adds it to a portfolio if provided.
        The requested_amount must be in denominations of $25.

        The POST request for the account/orders resource.

        See: https://www.lendingclub.com/developers/submit-order
        """

        order = {
            'loanId': loan_id,
            'requested_amount': requested_amount
        }
        if portfolio_id:
            order['portfolioId'] = portfolio_id

        try:
            submit_orders_response = self.submit_orders([order])
        except ValueError as e:
            raise e

        return submit_orders_response

    def __init__(self, url, headers, investor_id):
        self._investor_id = investor_id
        super(Account, self).__init__(self.join_url(url, investor_id), headers)

        # Sub-Resources
        self.funds = Funds(self.join_url(self._url, 'funds'), headers)

        # GET Requests
        self._summary = self._get_request('summary')
        self._available_cash = self._get_request('availablecash')
        self._notes = self._get_request('notes')
        self._detailednotes = self._get_request('detailednotes')
        self._portfolios = self._get_request('portfolios')
        self._filters = self._get_request('filters')

        # POST Requests
        self._create_portfolio = self._post_request('portfolios')
        self._submit_orders = self._post_request('orders')


class AccountSummary(ExtendedBase):
    def _refresh(self):
        summary = self._get_response_value(self._session.account.summary)
        self.__summary = self._unpack_dictionary(summary)

    @property
    def _expired(self):
        if self._refreshed_time is None:
            return True

        if (self._refreshed_time - time.time()) > self._lifespan_in_seconds:
            return True

        return False

    @property
    def _summary(self):
        if self._expired:
            self._refresh()

        return self.__summary

    @property
    def summary(self):
        return self._summary

    @property
    def investor_id(self):
        return self._summary['investorId']

    @property
    def available_cash(self):
        return self._summary['availableCash']

    @property
    def account_total(self):
        return self._summary['accountTotal']

    @property
    def accrued_interest(self):
        return self._summary['accruedInterest']

    @property
    def infunding_balance(self):
        return self._summary['infundingBalance']

    @property
    def received_interest(self):
        return self._summary['receivedInterest']

    @property
    def received_principal(self):
        return self._summary['receivedPrincipal']

    @property
    def received_late_fees(self):
        return self._summary['receivedLateFees']

    @property
    def outstanding_principal(self):
        return self._summary['outstandingPrincipal']

    @property
    def total_notes(self):
        return self._summary['totalNotes']

    @property
    def total_portfolios(self):
        return self._summary['totalPortfolios']

    @property
    def net_annualized_return(self):
        return self._summary['netAnnualizedReturn']

    @property
    def primary_NAR(self):
        return self._summary['primaryNAR']

    @property
    def primary_adjusted_NAR(self):
        return self._summary['primaryAdjustedNAR']

    @property
    def primary_user_adjusted_NAR(self):
        return self._summary['primaryUserAdjustedNAR']

    @property
    def traded_NAR(self):
        return self._summary['tradedNAR']

    @property
    def traded_adjusted_NAR(self):
        return self._summary['tradedAdjustedNAR']

    @property
    def traded_user_adjusted_NAR(self):
        return self._summary['tradedUserAdjustedNAR']

    @property
    def combined_NAR(self):
        return self._summary['combinedNAR']

    @property
    def combined_adjusted_NAR(self):
        return self._summary['combinedAdjustedNAR']

    @property
    def combined_user_adjusted_NAR(self):
        return self._summary['combinedUserAdjustedNAR']

    @property
    def adjustment_for_past_due_notes(self):
        return self._summary['adjustmentForPastDueNotes']

    @property
    def user_adjustment_for_past_due_notes(self):
        return self._summary['userAdjustmentForPastDueNotes']

    def __init__(self, session, lifespan=300):
        self._session = session
        self._lifespan_in_seconds = lifespan
        self._refreshed_time = None

        self.__summary = None
