from pylendingclub.wrapper.resource import Resource

class Funds(Resource):
    """
    Account/Funds resource within the LendingClub API.
    """
    @property
    def pending(self):
        """
        Pending transfers.

        The GET request for the account/funds/pending resource.

        See: https://www.lendingclub.com/developers/pending-transfers
        """
        return self._pending.send()

    def add(self, amount, transfer_frequency, start_date=None, end_date=None):
        """
        Transfer funds to the account.

        The POST request for the account/funds/add resource.

        See: https://www.lendingclub.com/developers/add-funds
        """
        if not transfer_frequency in self._transfer_frequencies:
            raise ValueError('Transfer frequency must be one of ' + ','.join(self._transfer_frequencies) + '.')

        payload = {
                    'amount' : amount,
                    'transferFrequency' : transfer_frequency
        }

        if start_date:
            payload['start_date'] = start_date

        if end_date:
            payload['end_date'] = end_date

        return self._add.send(payload=payload)

    def withdraw(self, amount):
        """
        Withdraw funds from the account.

        The POST request for the account/funds/withdraw resource.

        See: https://www.lendingclub.com/developers/add-funds
        """
        return self._withdraw.send(payload={ 'amount' : amount})

    def cancel(self, transfer_id):
        """
        Cancel a pending transfer.

        The POST request for the account/funds/cancel resource.

        See: https://www.lendingclub.com/developers/cancel-transfers
        """
        return self._cancel.send(payload={'transferIds' [transfer_id]})

    def __init__(self, url, headers):
        super().__init__(url, headers)

        self._transfer_frequencies = ['LOAD_NOW', 'LOAD_ONCE', 'LOAD_WEEKLY', 'LOAD_BIWEEKLY',
                                      'LOAD_ON_DAY_1_AND_16', 'LOAD_MONTHLY']

        #GET Requests
        self._pending = self._get_request('pending')

        #POST Requests
        self._add = self._post_request('add')
        self._withdraw = self._post_request('withdraw')
        self._cancel = self._post_request('cancel')
