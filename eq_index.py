class EqIFinder:

    def __init__(self):
        count = int(input('Enter number of elements:'))
        self.intlist = [int(input('Enter element #' + str(i) + ':')) for i in range(count)]
        # todo check input

    def get_eq_indices_2pass(self):
        eq_indices = []
        right_sum = sum(self.intlist)
        left_sum = 0
        for i, value in enumerate(self.intlist):
            left_sum += value
            right_sum -= value
            if left_sum == right_sum:
                eq_indices.append(i)
        return eq_indices

    def get_eq_indices_hash(self):
        import collections
        hashdict = collections.defaultdict(list)
        left_sum = 0
        for i, value in enumerate(self.intlist):
            left_sum += value
            hashdict[2 * left_sum - value].append(i)
        return hashdict[left_sum]


eq_finder = EqIFinder()
print(eq_finder.get_eq_indices_hash())

#
# Your previous Plain Text content is preserved below:
#
# '''
# A[0] + A[1] + ... + A[P−1] = A[P+1] + ... + A[N−2] + A[N−1].
# Sum of zero elements is assumed to be equal to 0. This can happen if P = 0 or if P = N−1.
#
# For example, consider the following array A consisting of N = 8 elements:
#
#   A[0] = -1
#   A[1] =  3
#   A[2] = -4
#   A[3] =  5
#   A[4] =  1
#   A[5] = -6
#   A[6] =  2
#   A[7] =  1
# P = 1 is an equilibrium index of this array, because:
#
# A[0] = −1 = A[2] + A[3] + A[4] + A[5] + A[6] + A[7]
# P = 3 is an equilibrium index of this array, because:
#
# A[0] + A[1] + A[2] = −2 = A[4] + A[5] + A[6] + A[7]
# P = 7 is also an equilibrium index, because:
#
# A[0] + A[1] + A[2] + A[3] + A[4] + A[5] + A[6] = 0
# and there are no elements with indices greater than 7.
#
# P = 8 is not an equilibrium index, because it does not fulfill the condition 0 ≤ P < N.
#
# Write a function:
#
# class Solution { public int solution(int[] A); }
#
# that, given a zero-indexed array A consisting of N integers, returns any of its equilibrium indices. The function should return −1 if no equilibrium index exists.
#
# For example, given array A shown above, the function may return 1, 3 or 7, as explained above.
#
# Assume that:
#
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
# Complexity:
#
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
# Elements of input arrays can be modified.
#
# Copyright 2009–2017 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
# Custom test casesformat: [-1, 3, -4, 5, 1, -6, 2, 1]  0/10
# '''
