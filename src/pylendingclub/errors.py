class AvailableCashError(Exception):
    def __init__(self, available_amount, requested_amount):
        error_message = (
                        'There is not enough available cash in the account. ' +
                        'Amount available is {available_amount}, amount requested is {requested_amount}. ' +
                        '\nPlease add funds or reduce the requested amount.'
                        ).format(available_amount=available_amount, requested_amount=requested_amount)

        super().__init__(error_message)


class InvalidAmountError(Exception):
    def __init__(self, amount, denomination):
        error_message = (
                        'The amount of {amount} is not in the denomination of {denomination}.'
                        ).format(amount=amount, denomination=denomination)

        super().__init__(error_message)


class UnevenDivisionError(Exception):
    def __init__(self, numerator, denominator):
        error_message = (
                        'The provided amount of {numerator} is not evenly divisable by {denominator}'
                        ).format(numerator=numerator, denominator=denominator)

        super().__init__(error_message)


class AvailableLoansError(Exception):
    def __init__(self):
        error_message = ('There are no notes available that match the provided criteria. ' +
                         ' Either specify an alternative filter, or wait until additional ' +
                         ' notes have been listed on the market.')

        super().__init__(error_message)
