class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")
            unique_emails.add(f"{local}@{domain}")

        # print(len(unique_emails))
        return len(unique_emails)