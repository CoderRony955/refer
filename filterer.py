import re

class Filter:
    @staticmethod
    def word(name: str):
        """Filter given string from no-characters
        """
        return re.sub(r"[\"\'*()^%]", '', name)

