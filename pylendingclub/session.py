from .base import Base
from .account import Account
from .loan import Loan

class LendingClubSession(Base):
    """
    Serves as the primary wrapper for the LendingClub API.

    The API resources are available as public properties.
    """

    def __init__(self, version, api_key, investor_id):
        self._url = 'https://api.lendingclub.com/api/investor/{}/'.format(version)
        self._headers = {'Authorization' : api_key}
        self.account = Account(self.join_url(self._url, 'accounts', True), self._headers, investor_id)
        self.loan = Loan(self.join_url(self._url, 'loans', True), self._headers)
