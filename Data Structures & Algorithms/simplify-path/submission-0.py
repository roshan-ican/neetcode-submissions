class Solution:
    def simplifyPath(self, path: str) -> str:
        # if the top of stack is like not / 
        # we keep on popping

        stack = []
        components = path.split("/")

        for co in components:
            if co  == "" or co == ".":
                continue
            elif co == "..":
                if stack:
                    stack.pop()

            else:
                stack.append(co)
        return "/" + "/".join(stack)