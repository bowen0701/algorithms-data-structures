"""Leetcode 973. K Closest Points to Origin
Medium

URL: https://leetcode.com/problems/k-closest-points-to-origin/

We have a list of points on the plane.  Find the K closest points to the
origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique
(except for the order that it is in.)


Example 1:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 
Note:
- 1 <= K <= points.length <= 10000
- -10000 < points[i][0] < 10000
- -10000 < points[i][1] < 10000
"""

class SolutionMaxHeap(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]

        Time complexity: O(n*logk).
        Space complexity: O(k).
        """
        import heapq

        # Use maxheap by heapq with "negative" distances.
        maxheap = []

        negdistances = [-(p[0] ** 2 + p[1] ** 2) for p in points]
        negdistances_points = zip(negdistances, points)

        # Push the first K points into maxheap and keep the length.
        # Then push the remaining points if negative distance > maxheap's root.
        for i, (nd, p) in enumerate(negdistances_points):
            if i < K:
                heapq.heappush(maxheap, (nd, p))
            elif i >= K:
                if nd > maxheap[0][0]:
                    heapq.heappush(maxheap, (nd, p))
                    heapq.heappop(maxheap)

        k_points = [p for (nd, p) in maxheap]
        return k_points


class SolutionSelection(object):
    def _selectKClosest(self, distances, K):
        # Select smaller & larger nums by pivot.
        n = len(distances)
        pivot = distances[n // 2]

        smaller_pos = [pos for (pos, d) in enumerate(distances) if d < pivot]
        pivot_pos = [pos for (pos, d) in enumerate(distances) if d == pivot]
        larger_pos = [pos for (pos, d) in enumerate(distances) if d > pivot]

        n_smaller = len(smaller_pos)
        n_pivot = len(pivot_pos)

        if K <= n_smaller:
            smaller_distance = [distances[pos] for pos in smaller_pos]
            return self._selectKClosest(smaller_distance, K)
        elif n_smaller < K <= n_smaller + n_pivot:
            return pivot
        else:
            larger_distances = [distances[pos] for pos in larger_pos]
            return self._selectKClosest(larger_distances, K - n_smaller - n_pivot)

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        distances = [p[0] ** 2 + p[1] ** 2 for p in points]
        pivot = self._selectKClosest(distances, K)

        k_points = []
        for (d, p) in zip(distances, points):
            if d <= pivot:
                # For fast list append.
                k_points += p,
        
        return k_points


def main():
    # Ans: [[-2,2]]
    points = [[1,3],[-2,2]]
    K = 1
    # print SolutionMaxHeap().kClosest(points, K)
    print SolutionSelection().kClosest(points, K)

    # Ans: [[3,3],[-2,4]]
    points = [[3,3],[5,-1],[-2,4]]
    K = 2
    # print SolutionMaxHeap().kClosest(points, K)
    print SolutionSelection().kClosest(points, K)


if __name__ == '__main__':
    main()