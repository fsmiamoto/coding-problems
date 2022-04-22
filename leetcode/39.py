class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def combinations(possibleValues: List[int], cIndex: int, currComb: List[int], currSum: int, target: int):
            if target < 0:
                # No negative values
                return

            if target == 0:
                result.append(currComb)
                return

            if cIndex >= len(candidates):
                return


            c = candidates[cIndex]
            possibleValues.append(c)

            combinations(possibleValues,cIndex,currComb + [c], currSum + c, target-c)

            possibleValues.pop()
            combinations(possibleValues,cIndex+1, currComb, currSum, target)

        combinations([], 0, [], 0, target)

        return result
