class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        hash_set = set()

        for i in range(len(emails)):
            [name, domain_name] = emails[i].split("@")
            mod_name = ''
            for j in range(len(name)):
                if name[j] == ".":
                    continue
                if name[j] == "+":
                    break
                else:
                    mod_name += name[j]
            hash_set.add(mod_name+"@"+domain_name)
        return len(hash_set)
