class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Since all numbers are positive, we can right away exclude any elements that have an element bigger than the in target
        # We must actually merge at most 3 triplets, each containing one or more elements of the target.
        found = 0b000
        bTarget = 0b111
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                if triplet[0] == target[0]:
                    found |= 0b100
                if triplet[1] == target[1]:
                    found |= 0b010
                if triplet[2] == target[2]:
                    found |= 0b001

                if found == bTarget:
                    return True
        return False