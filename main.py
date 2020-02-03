from typing import List


class Solution:

  def singleNumber(self, nums: List[int]) -> int:
    dict = {}

    for value in nums:
      if value in dict:
        dict[value] += 1
      else:
        dict[value] = 1

    for item in dict:
      if dict[item] == 1:
        return item