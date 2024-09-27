class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to map each closing bracket to its corresponding open bracket
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if available, else use a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the expected open bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # Push the open bracket onto the stack
                stack.append(char)

        # Return True if stack is empty, meaning all brackets were matched correctly
        return not stack
