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
