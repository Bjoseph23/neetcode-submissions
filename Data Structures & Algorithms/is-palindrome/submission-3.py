class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter out non-alphanumeric characters and convert to lowercase
        cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
        # Compare the cleaned string to its reversed version
        return cleaned_str == cleaned_str[::-1]