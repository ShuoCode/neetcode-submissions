class Solution:
    def isValid(self, s: str) -> bool:
        # there will always be paired parentheses next to each other
        # in the string
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
        return s == ''
