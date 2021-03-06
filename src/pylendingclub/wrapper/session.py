import os

import pandas as pd

from ..config import LC_API_URL
from ..config import LC_SANDBOX_API_URL
from ..errors import AvailableCashError
from ..errors import AvailableLoansError
from ..errors import InvalidAmountError
from ..errors import UnevenDivisionError
from .account import Account
from .account import AccountSummary
from .base import Base
from .base import ExtendedBase
from .loan import Loan
from .order import Order


class LendingClubSession(Base):
    """
    Serves as the primary wrapper for the LendingClub API.

    The API resources are available as public properties.
    """
    def __init__(self, api_key, investor_id, url=LC_API_URL):
        self._url = url
        self._headers = {'Authorization': api_key}
        self.account = Account(self.join_url(self._url, 'accounts', True),
                               self._headers, investor_id)
        self.loan = Loan(self.join_url(self._url, 'loans', True), self._headers)

    @classmethod
    def from_environment_variables(cls, test_mode=False):
        if not test_mode:
            return cls(os.environ['LC_API_KEY'],
                       os.environ['LC_INVESTOR_ID'])
        else:
            return cls(os.environ['LC_SANDBOX_API_KEY'],
                       os.environ['LC_SANDBOX_INVESTOR_ID'],
                       LC_SANDBOX_API_URL)


class ExtendedLendingClubSession(ExtendedBase):
    def _validate_amount(self, amount, denomination=25):
        if (amount % denomination) != 0:
            raise InvalidAmountError(amount, denomination)

    def _num_notes(self, total_amount, amount_per_note):
        if (total_amount // amount_per_note) != (total_amount / amount_per_note):
            raise UnevenDivisionError(total_amount, amount_per_note)
        else:
            return int(total_amount / amount_per_note)

    def _filter_id_by_name(self, name):
        filters_response = self.session.account.filters
        filters_data = filters_response.json()['filters']
        filter_dict = self._dict_by_key_value_pair(filters_data, 'name', name)
        if filter_dict:
            return filter_dict['id']

    def _portfolio_id_by_name(self, name):
        portfolios_owned_response = self.session.account.portfolios_owned
        portfolios_data = portfolios_owned_response.json()['myPortfolios']
        filter_dict = self._dict_by_key_value_pair(portfolios_data, 'portfolioName', name)
        if filter_dict:
            return filter_dict['portfolioId']

    def _listed_loans(self,
                      filter_id=None,
                      sort_fields={'loanAmount': True,
                                   'intRate': False,
                                   'empLength': False},
                      listing_filter=None,
                      remove_owned_notes=True):

        listed_loans_response = self.session.loan.listed_loans(filter_id=filter_id)
        listed_loans_data = listed_loans_response.json()

        if 'loans' in listed_loans_data:
            loans_df = pd.DataFrame(listed_loans_data['loans'])
            loans_df['percentFunded'] = loans_df['fundedAmount']/loans_df['loanAmount']

            if listing_filter is not None:
                loans_df = listing_filter.filter_listings(loans_df)

            if remove_owned_notes:
                loans_df = loans_df[~loans_df['id'].isin(self.owned_loans)]

            if loans_df is not None:
                if isinstance(sort_fields, dict):
                    fields = []
                    directions = []
                    for field, direction in sort_fields.items():
                        fields.append(field)

                        if isinstance(direction, (bool, int)):
                            directions.append(bool(direction))
                        else:
                            directions.append(False)

                        loans_df = loans_df.sort_values(fields, ascending=directions)
            return loans_df

    def invest(self,
               total_amount=25,
               amount_per_note=25,
               filter_id=None,
               portfolio_id=None,
               listing_filter=None,
               reinvest_when_owned=False):
        available_cash = self.available_cash(as_string=False)
        if total_amount > available_cash:
            raise AvailableCashError(available_cash, total_amount)
        try:
            num_notes = self._num_notes(total_amount, amount_per_note)
            self._validate_amount(total_amount)
            self._validate_amount(amount_per_note)
        except ValueError as e:
            raise e

        listed_loans = self._listed_loans(filter_id=filter_id,
                                          listing_filter=listing_filter,
                                          remove_owned_notes=not reinvest_when_owned)

        if listed_loans is not None:
            orders = [Order(loan_id, amount_per_note, portfolio_id)
                      for loan_id in listed_loans.head(num_notes)['id'].values]

            return self.submit_orders(orders)
        else:
            raise AvailableLoansError()

    @property
    def account_summary(self):
        return self._account_summary

    @property
    def owned_loans(self):
        try:
            return list(notes['loanId'].unique())
        except:
            return []

    def available_cash(self, as_string=True):
        response_value = self._get_response_value(self.session.account.available_cash,
                                                  key='availableCash')
        if as_string and response_value:
            return '${:,.2f}'.format(response_value)
        else:
            return response_value

    def notes(self, as_dataframe=True):
        return self._get_response_value(self.session.account.notes,
                                        key='myNotes',
                                        as_dataframe=as_dataframe)

    def detailed_notes(self, as_dataframe=True):
        return self._get_response_value(self.session.account.detailed_notes,
                                        key='myNotes',
                                        as_dataframe=as_dataframe)

    def create_portfolio(self, name, description=None):
        return self.account.create_portfolio(name, description)

    def portfolios(self, as_dataframe=True):
        return self._get_response_value(self.session.account.portfolios_owned,
                                        key='myPortfolios',
                                        as_dataframe=as_dataframe)

    def portfolio_id_by_name(self, name):
        return self._portfolio_id_by_name(name)

    def filters(self, as_dataframe=True):
        return self._get_response_value(self.session.account.filters,
                                        key='filters',
                                        as_dataframe=as_dataframe)

    def filter_id_by_name(self, name):
        return self._filter_id_by_name(name)

    def listed_loans(self, filter_id=None, listing_filter=None):
        return self._listed_loans(filter_id=filter_id)

    def submit_order(self, loan_id, amount, portfolio=None):
        order = [Order(loan_id, amount, portfolio)]
        return self.submit_orders(order)

    def submit_orders(self, orders):
        packaged_orders = []
        for order in orders:
            if isinstance(order, Order):
                packaged_orders.append(order.order())
            else:
                packaged_orders.append(Order.from_dict(order).order())

        return self.session.account.submit_orders(packaged_orders)

    def add_funds(self, amount, transfer_frequency='LOAD_NOW', start_date=None, end_date=None):
        return self.session.account.funds.add(amount, transfer_frequency, start_date, end_date)

    def withdraw_funds(self, amount):
        return self.session.account.funds.withdraw(amount)

    def pending_transfers(self):
        return self.session.account.funds.pending

    def cancel_transfer(self, transfer_id):
        return self.session.account.funds.cancel(transfer_id)

    def __init__(self, account_summary_lifespan=300):
        self.session = LendingClubSession.from_environment_variables()
        self._account_summary = AccountSummary(self.session, account_summary_lifespan)
