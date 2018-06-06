class Base():
    """
    Provides basic functions for handling URL's when creating requests and resources.
    """

    def _add_trailing_slash(self, url):
        """
        Ensures the URL has a trailing slash.
        """
        return url if url.endswith('/') else (url + '/')

    def _remove_leading_slash(self, url):
        """
        Removes the leading slash from the URL.
        """
        return url if not url.startswith('/') else url[1:]

    def join_url(self, base_url, sub_url, add_trailing_slash=False):
        """
        Joins a base url together with the sub-directory.
        """
        return  self._add_trailing_slash(base_url) + self._remove_leading_slash(sub_url)
