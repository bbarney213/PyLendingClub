import pandas as pd


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
        return self._add_trailing_slash(base_url) + self._remove_leading_slash(sub_url)


class ExtendedBase(Base):
    def _unpack_dictionary(self, input_dictionary):
        unpacked_dictionary = {}
        for key, value in input_dictionary.items():
            if isinstance(value, dict):
                for key, value in self._unpack_dictionary(value).items():
                    unpacked_dictionary[key] = value
            else:
                unpacked_dictionary[key] = value
        return unpacked_dictionary

    def _get_response_value(self, response, key=None, as_dataframe=False, raise_for_status=False):
        if raise_for_status:
            response.raise_for_status()

        if response.status_code == 200:
            response_value = None

            if key:
                if key in response.json():
                    response_value = response.json()[key]
                else:
                    raise KeyError('The provided key {key} does not ' +
                                   'exist within the keys of the json response.').format(key=key)
            else:
                response_value = response.json()

            if as_dataframe:
                return pd.DataFrame(response_value)

            return response_value

    def _dict_by_key_value_pair(self, dicts, key, value):
        for dict_item in dicts:
            if dict_item[key] == value:
                return dict_item
