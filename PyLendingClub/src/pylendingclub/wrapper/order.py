class Order():
    def order(self):
        return {
                'loanId' : self._loan_id,
                'requestedAmount' : self._amount,
                'portfolioId' : self._portfolio
               }

    def __init__(self, loan_id, amount, portfolio):
        self._loan_id = int(loan_id)
        self._amount = amount
        self._portfolio = portfolio

    @classmethod
    def from_dict(cls, input_dict):
        return cls(input_dict.get('loanId'),
                   input_dict.get('requestedAmount'),
                   input_dict.get('portfolioId'))

class ConfirmedOrder():
    #TODO : Surface properties of the notes being purchased

    @property
    def fulfilled(self):
        return self._fulfilled

    def data(self):
        source = dict(self._source)
        source['fulfilled'] = self.fulfilled
        return source

    def __init__(self, json):
        self._source = json
        self._loan_id = json.get('loanId')
        self._requested_amount = json.get('requestedAmount')
        self._invested_amount = json.get('investedAmount')
        self._execution_status = json.get('executionStatus')
        self._fulfilled = 'ORDER_FULFILLED' in self._execution_status
