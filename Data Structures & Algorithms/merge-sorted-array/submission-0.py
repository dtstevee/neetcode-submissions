class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Three pointers
        p1 = m - 1      # Last valid element in nums1
        p2 = n - 1      # Last element in nums2
        p = m + n - 1   # Last position in nums1 to fill
        
        # While we still have elements in nums2
        while p2 >= 0:
            # If p1 is valid AND nums1[p1] > nums2[p2], use nums1's element
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # Otherwise, use nums2's element
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        