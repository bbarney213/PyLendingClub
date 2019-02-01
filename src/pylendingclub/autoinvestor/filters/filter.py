class AbstractListedLoanFilter(object):
    def _filter_listings(self, listings):
        raise NotImplementedError("The _filter_listings function must be defined by the child class.")

    def filter_listings(self, listings):
        return self._filter_listings(listings)

    def __init__(self):
        pass
