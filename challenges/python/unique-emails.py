# Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = {}
        num_uniques = 0
        
        for email in emails:
            local, domain = email.split("@")
            index = local.find("+")
            if index > -1:
                local = local[:index]
            local = local.replace(".","")
            cleaned = local + "@" + domain
            # print(cleaned)
            if cleaned not in uniques:
                uniques[cleaned] = True
                num_uniques += 1
                
        return num_uniques
            
