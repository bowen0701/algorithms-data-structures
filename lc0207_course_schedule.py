"""Leetcode 207. Course Schedule
Medium

URL: https://leetcode.com/problems/course-schedule/

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have
to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?

Example 1:
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take
course 0 you should also have finished course 1. So it is impossible.

Note:
- The input prerequisites is a graph represented by a list of edges,
  not adjacency matrices. Read more about how a graph is represented.
- You may assume that there are no duplicate edges in the input prerequisites.
"""

class SolutionBFSTopologicalSort(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        Time complexity: O(|V|+|E|), where
          - |V|: number of vertices, i.e. courses.
          - |E|: number of edges.
        Space complexity: O(|V|).
        """
        # Apply BFS Topological Sort to take courses.
        from collections import defaultdict
        from collections import deque

        # Collect dict:prereq->list(courses) & courses's indegrees n_prereqs.
        prereq_courses_d = defaultdict(list)
        n_prereqs = [0] * numCourses

        for course, prereq in prerequisites:
            prereq_courses_d[prereq].append(course)
            n_prereqs[course] += 1

        # Create a queue for courses w/o prereq so that they can be taken.
        queue = deque()
        for course in range(numCourses):
            if n_prereqs[course] == 0:
                queue.appendleft(course)

        while queue:
            # Take course w/o prerequisites.
            course = queue.pop()
            numCourses -= 1

            for nxt in prereq_courses_d[course]:
                # Decrement number of prerequisites of next course.
                n_prereqs[nxt] -= 1

                # If no more prerequisites, add to queue as course candidate.
                if n_prereqs[nxt] == 0:
                    queue.appendleft(nxt)

        return numCourses == 0


def main():
    # Output: true
    numCourses = 2
    prerequisites = [[1,0]]
    print SolutionBFSTopologicalSort().canFinish(numCourses, prerequisites)

    # Output: false
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print SolutionBFSTopologicalSort().canFinish(numCourses, prerequisites)

    # Output: false
    numCourses = 3
    prerequisites = [[1,0],[2,1],[0,2]]
    print SolutionBFSTopologicalSort().canFinish(numCourses, prerequisites)


if __name__ == '__main__':
    main()
