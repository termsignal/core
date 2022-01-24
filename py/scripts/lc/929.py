
# * * Approach 2: Using String Split Method
# * * Intuition
# * *
# * * A more elegant way of cleaning emails is to leverage built-in functions such as split and replace.
# * *
# * * The string split() method breaks a given string around matches of the given regular expression.
# * * The string replace() method returns a new string after replacing all occurrences of some substring or character (in this case '.') with a new substring or character (in this case '').
# * * Algorithm
# * *
# * * For each email present in the emails array:
# * * Split the string into two parts separated by'@', local name, and domain name.
# * * Split the local name into parts separated by '+'. Since we do not need the part after '+', let the first part be the local name.
# * * Remove all '.' from the local name and append the domain name to it.
# * * After cleaning the email, insert it into the hash set.
# * * Return the size of the hash set.


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # * * Hash set to store all the unique emails.
        uniqueEmails = set()

        for email in emails:
            # * * Split into two parts: local and domain.
            name, domain = email.split('@')

            # * * Split local by '+' and replace all '.' with ''.
            local = name.split('+')[0].replace('.', '')

            # * * Concatenate local, '@', and domain.
            uniqueEmails.add(local + '@' + domain)

        return len(uniqueEmails)