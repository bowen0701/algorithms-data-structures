"""Leetcode 39. Combination Sum
Medium

URL: https://leetcode.com/problems/combination-sum/

Given a set of candidate numbers (candidates) (without duplicates) and a
target number (target), find all unique combinations in candidates where
the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:
- All numbers (including target) will be positive integers.
- The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class SolutionBacktrack(object):
    def _backtrack(self, result, temp, start, target, candidates):
        if target < 0:
            # No way to further combine numbers.
            return None

        if target == 0:
            # Use shallow copy.
            result.append(temp[:])
            return None

        # Iterate starting from start.
        for i in range(start, len(candidates)):
            temp.append(candidates[i])

            # Keep using i because can reuse the same number.
            self._backtrack(result, temp, i, target - candidates[i], candidates)
            
            # Pop for backtracking.
            temp.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        Apply backtracking.

        Time complexity: O(n^k), where
          - n is the length of candidates,
          - k is target.
        Space complexity: O(k).
        """
        result = []
        temp = []
        start = 0
        self._backtrack(result, temp, start, target, candidates)
        return result


def main():
    # Output: [[7],[2,2,3]]
    candidates = [2,3,6,7]
    target = 7
    print SolutionBacktrack().combinationSum(candidates, target)

    # Output: [[2,2,2,2],[2,3,3],[3,5]]
    candidates = [2,3,5]
    target = 8
    print SolutionBacktrack().combinationSum(candidates, target)


if __name__ == '__main__':
    main()
