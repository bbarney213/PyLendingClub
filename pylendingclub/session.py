import os

from pylendingclub.base import Base
from pylendingclub.account import Account
from pylendingclub.loan import Loan
from pylendingclub.config import LC_API_VERSION

class LendingClubSession(Base):
    """
    Serves as the primary wrapper for the LendingClub API.

    The API resources are available as public properties.
    """

    def __init__(self, api_key, investor_id):
        self._url = 'https://api.lendingclub.com/api/investor/{}/'.format(LC_API_VERSION)
        self._headers = {'Authorization' : api_key}
        self.account = Account(self.join_url(self._url, 'accounts', True), self._headers, investor_id)
        self.loan = Loan(self.join_url(self._url, 'loans', True), self._headers)

    @classmethod
    def from_environment_variables(cls):
        return cls(os.environ['LC_API_KEY'], os.environ['LC_INVESTOR_ID'])
