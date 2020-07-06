"""Leetcode 55. Jump Game
Medium

URL: https://leetcode.com/problems/jump-game/

Given an array of non-negative integers, you are initially positioned at the 
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
jump length is 0, which makes it impossible to reach the last index.
"""


class SolutionRecur(object):
    def jumpRecur(self, start, end, nums):
        # Base case.
        if start == end:
            return True

        for jump in range(1, nums[start] + 1):
            if self.jumpRecur(start + jump, end, nums):
                return True
        return False

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        start, end = 0, n - 1
        return self.jumpRecur(start, end, nums)


class SolutionDP(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Apply bottom-up DP with table T, where T[i]=True means reachable.
        n = len(nums)
        T = [False] * n
        T[0] = True

        # Iterate through nums to check reachable from previous reachable index.
        for r in range(1, n):
            for l in range(r - 1, -1, -1):
                if r - l <= nums[l] and T[l]:
                    T[r] = True
                    break
        return T[-1]


class SolutionGreedy(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Apply greedy approach with early stopping.
        # Set reach for max reachable index.
        reach = 0

        # Iterate through nums to check if index i is not reachable.
        for i in range(len(nums)):
            if reach < i:
                return False

            # Greedily update max reach.
            reach = max(reach, i + nums[i])

        return True


def main():
    import time

    # Ans: True
    nums = [2,3,1,1,4]

    start_time = time.time()
    print 'Recur:', SolutionRecur().canJump(nums)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'DP:', SolutionDP().canJump(nums)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'DP:', SolutionGreedy().canJump(nums)
    print 'Time:', time.time() - start_time

    # Ans: False
    nums = [3,2,1,0,4]

    start_time = time.time()
    print 'Recur:', SolutionRecur().canJump(nums)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'DP:', SolutionDP().canJump(nums)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'DP:', SolutionGreedy().canJump(nums)
    print 'Time:', time.time() - start_time


if __name__ == '__main__':
    main()
