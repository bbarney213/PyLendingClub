from pylendingclub.resource import Resource

class Loan(Resource):
    """
    Loan resource for the LendingClub API.
    """

    def listed_loans(self, filter_id=None, show_all=True):
        """
        The loans currenly listed.

        By default shows all loans currently listed. If show_all is set to False
        only the loans listed in the most recent listing period will be shown.

        If a filter_id is provided, only loans matching the filter will be provided.
        """
        return self._listed_loans.send(query_params={'filterId' : filter_id, 'showAll' : show_all})

    def __init__(self, url, headers):
        super().__init__(url, headers)
        self._listed_loans = self._get_request('listing')
