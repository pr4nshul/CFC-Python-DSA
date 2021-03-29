"""
https://leetcode.com/problems/remove-outermost-parentheses/
"""

class Solution1:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        stack = []
        answer = ""
        if not S:
            return ""
        for ch in S:
            stack.append(ch)
            if ch == "(":
                count += 1
            else:
                count -= 1
                if count == 1:
                    temp = ""
                    while  len(stack) > 1:
                        ch_popped = stack.pop()
                        temp = ch_popped + temp
                    answer += temp

                if count == 0:
                    while len(stack) != 0:
                        stack.pop()
        return answer

"""
https://leetcode.com/problems/next-greater-element-i/
"""

class Solution2:
    def nextGreaterElement(self, nums1, nums2):
        map = {}
        stack = []
        next_greater_list = []
        for index,num in enumerate(nums2):
            if len(stack) == 0:
                stack.append(num)
            else:
                while len(stack) >0 and  stack[-1] < num :
                    element = stack.pop()
                    map[element] = num

                stack.append(num)
        while len(stack) > 0:
            element = stack.pop()
            map[element] = -1

        for i in nums1:
            element= map.get(i)
            next_greater_list.append(element)

        return next_greater_list

"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
"""

class Solution3:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        if not S:
            return ""

        for ch in S:
            if len(stack) == 0:
                stack.append(ch)
            else:
                if ch == stack[-1]:
                    stack.pop()
                else:
                    stack.append(ch)

        return "".join(stack)

"""
https://leetcode.com/problems/valid-parentheses/
"""
class Solution4:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for ch in s:
            if ch == "(" or ch =="[" or ch =="{":
                stack.append(ch)
            else:
                if (ch == ")" or ch == "]" or ch == "}")  and len(stack) > 0:
                    condition1 = ch == ")" and stack[-1] == "("
                    condition2 = ch == "]" and stack[-1] == "["
                    condition3 = ch == "}" and stack[-1] == "{"

                    if condition1 or condition2 or condition3:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        if len(stack) > 0:
            return False
        else:
            return True

"""
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
"""

class Solution5:
    def minAddToMakeValid(self, S: str) -> int:
        count = 0
        stack = []
        for ch in S:
            if ch == "(":
                stack.append(ch)
            else:
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(ch)

        return len(stack)

"""
 https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
"""
class Solution6:
    def minAddToMakeValid(self, S: str) -> int:
        count = 0
        stack = []
        for ch in S:
            if ch == "(":
                stack.append(ch)
            else:
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(ch)

        return len(stack)

"""
https://leetcode.com/problems/decode-string/
"""

class Solution7:
    def decodeString(self, s: str) -> str:
        stack = []
        answer = ""
        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                temp = ""
                i = ""
                while len(stack) > 0 and stack[-1] != "[":
                    temp = stack.pop() + temp

                stack.pop()

                while len(stack) >0 and stack[-1].isnumeric():
                    i = stack.pop() + i

                value = int(i)
                while value > 0:
                    stack.append(temp)
                    value -= 1

        while len(stack):
            answer = stack.pop() + answer

        return answer
"""
https://leetcode.com/problems/min-stack/
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            if val < self.min_stack[-1]:
                self.min_stack.append(val)
            else:
                minimum = self.min_stack[-1]
                self.min_stack.append(minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]



    def isEmpty(self):
        return len(self.stack) == 0



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
https://leetcode.com/problems/implement-queue-using-stacks/
"""
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        element = self.stack2.pop()
        while len(self.stack2) >0 :
            self.stack1.append(self.stack2.pop())
        return element


    def peek(self) -> int:
        """
        Get the front element.
        """
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        element = self.stack2[-1]
        while len(self.stack2) > 0 :
            self.stack1.append(self.stack2.pop())
        return element


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

"""
https://leetcode.com/problems/asteroid-collision/
"""

class Solution8:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                elif abs(stack[-1]) > abs(asteroid):
                    break
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    break
            else:
                stack.append(asteroid)

        return stack
"""
https://leetcode.com/problems/132-pattern/
"""

class Solution9:
    def find132pattern(self, nums: List[int]) -> bool:
        min_list = []
        stack = []
        if not nums:
            return False
        min_list.append(nums[0])

        for i in range(1,len(nums)):
            min_list.append(min(nums[:i]))

        for j in range(len(nums) -1,-1,-1):
            if nums[j] > min_list[j]:
                while stack and stack[-1] <= min_list[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True

            stack.append(nums[j])
        return False

"""
https://leetcode.com/problems/number-of-recent-calls/
"""

class RecentCounter:

    def __init__(self):
        self.counter = 0
        self.timer= []


    def ping(self, t: int) -> int:
        value = t-3000
        while self.timer and self.timer[0] < value:
            self.timer.pop(0)
        self.timer.append(t)
        return len(self.timer)

