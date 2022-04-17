class Solution:
    def hammingWeight(self, n: int) -> int:
      # Trick
      result = 0
      while n:
        # Remove a bit, this loop will run the amount of 1's in n
        n &= (n-1)
        result += 1

      return result

    def _hammingWeight(self, n: int) -> int:
      if n == 0:
        return 0
      return (n&1) + self.hammingWeight(n >> 1)
