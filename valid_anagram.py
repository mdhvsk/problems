class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_tally = [0] * 26
        t_tally = [0] * 26

        for letter in s:
            value = self.hash_func(letter)
            s_tally[value] += 1

        for letter in t:
            value = self.hash_func(letter)
            t_tally[value] += 1

        if s_tally == t_tally:
            return True
        else:
            return False

    def hash_func(self, letter):
        return ord(letter) % 26

    