from pylendingclub.resource import Resource
from pylendingclub.funds import Funds

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
                    'actorId' : self._investor_id,
                    'portfolioName' : portfolio_name
        }

        if portfolio_description:
            payload['portfolioDescription'] = portfolio_description

        return self._create_portfolio.send(payload=payload)

    def submit_order(self, loan_id, requested_amount, portfolio_id=None):
        """
        Submits an order for a note, and adds it to a portfolio if provided.
        The requested_amount must be in denominations of $25.

        The POST request for the account/orders resource.

        See: https://www.lendingclub.com/developers/submit-order
        """
        if (requested_amount % 25) != 0:
            raise ValueError('The requested amount must be a denomination of $25.00.')

        order = {
                    'loanId' : loan_id,
                    'requested_amount' : requested_amount
        }

        if portfolio_id:
            order['portfolioId'] = portfolio_id

        payload = {
                    'aid' : self._investor_id,
                    'orders' :
                    [
                        order
                    ]
        }
        return self._submit_order.send(payload=payload)

    def __init__(self, url, headers, investor_id):
        self._investor_id = investor_id
        super().__init__(self.join_url(url, investor_id), headers)

        #Sub-Resources
        self.funds = Funds(self.join_url(self._url, 'funds'), headers)

        #GET Requests
        self._summary = self._get_request('summary')
        self._available_cash = self._get_request('availablecash')
        self._notes = self._get_request('notes')
        self._detailednotes = self._get_request('detailednotes')
        self._portfolios =self._get_request('portfolios')
        self._filters = self._get_request('filters')

        #POST Requests
        self._create_portfolio = self._post_request('portfolios')
        self._submit_order = self._post_request('orders')
