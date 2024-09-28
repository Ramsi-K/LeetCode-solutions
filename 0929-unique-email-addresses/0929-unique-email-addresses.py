class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            # Find the index of '@' and '+' characters
            at_index = email.find('@')
            plus_index = email.find('+')

            # Extract the local and domain parts
            local = email[:plus_index] if plus_index != -1 else email[:at_index]
            domain = email[at_index:]

            # Remove all '.' from the local part
            local = local.replace('.', '')

            # Add the processed email (local@domain) to the set
            unique_emails.add(local + domain)


        # print(len(unique_emails))
        return len(unique_emails)