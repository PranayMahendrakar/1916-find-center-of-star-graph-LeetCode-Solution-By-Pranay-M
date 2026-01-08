class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # The center node appears in every edge
        # So it must appear in both the first two edges
        # Time: O(1), Space: O(1)
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]