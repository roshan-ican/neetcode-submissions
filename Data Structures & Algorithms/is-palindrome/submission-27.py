
class Solution:
  def isPalindrome(self, s: str) -> bool:
    # Filter only alphanumeric characters and convert to lowercase
    filtered = ''.join(char.lower() for char in s if char.isalnum())
    start = 0
    end = len(filtered) - 1

    while start < end:
        if filtered[start] != filtered[end]:
            return False
        start += 1
        end -= 1
    return True

        