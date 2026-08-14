from collections import defaultdict
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        domainsAndUsers = defaultdict(set)

        for email in emails:
            user, domain = email.split("@")
            user = user.replace(".", "")
            domainsAndUsers[domain].add(user.split("+")[0])

        res = 0
        for users in domainsAndUsers.values():
            res += len(users)

        return res
