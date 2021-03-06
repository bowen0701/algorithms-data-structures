"""Leetcode 45. Jump Game II
Hard

URL: https://leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers, you are initially positioned at
the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:
You can assume that you can always reach the last index.
"""


class SolutionDPGreedy(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n^2), where n is length of nums.
        Space complexity: O(n).
        """
        n = len(nums)

        # Apply DP with table T, where T[i] is min jumps to reach i.
        T = list(range(n))
        T[0] = 0

        # Iterate through to update T[reach+1],..., T[i+nums[i]].
        reach = 0
        for l in range(n):
            for r in range(reach + 1, min(l + nums[l], n - 1) + 1):
                T[r] = min(T[r], T[l] + 1)

            reach = max(reach, l + nums[l])

        return T[-1]


class SolutionBFSPrevReachGreedy(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n), where n is length of nums.
        Space complexity: O(1).
        """
        n = len(nums)

        # Apply greedy algorithm to check index i in prev_reach and reach.
        prev_reach, reach = -1, 0
        n_jumps = 0

        for i in range(n):
            # Check if reached last index already.
            if reach >= n - 1:
                break

            # Update n_jumps if prev_reach is behind current index i.
            if prev_reach < i:
                n_jumps += 1
                prev_reach = reach

            # Update reach with max jump from current index.
            reach = max(reach, i + nums[i])

        return n_jumps


class SolutionBFSCurReachGreedy(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n), where n is length of nums.
        Space complexity: O(1).
        """
        n = len(nums)

        # Apply greedy algorithm to check index i in cur_reach and reach.
        cur_reach, reach = 0, 0
        n_jumps = 0

        for i in range(n - 1):
            # Break if reaches last index.
            if cur_reach >= n - 1:
                break

            # Update n_jumps with max jump from current index i.
            reach = max(reach, i + nums[i])

            # If i reaches cur_reach, trigger another jump and update cur_reach.
            if i == cur_reach:
                n_jumps += 1
                cur_reach = reach

        return n_jumps


def main():
    # Outpout: 2
    nums = [2,3,1,1,4]
    print SolutionDPGreedy().jump(nums)
    print SolutionBFSPrevReachGreedy().jump(nums)
    print SolutionBFSCurReachGreedy().jump(nums)

    # Outpout: 2
    nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
    print SolutionDPGreedy().jump(nums)
    print SolutionBFSPrevReachGreedy().jump(nums)
    print SolutionBFSCurReachGreedy().jump(nums)


if __name__ == '__main__':
    main()
