class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        current_end = 0  # end of current jump window
        farthest = 0  # farthest index reachable so far

        for i in range(n - 1):  # don't need to jump from last index
            farthest = max(farthest, i + nums[i])  # extend reach

            if i == current_end:  # exhausted current window
                jumps += 1  # must take a jump
                current_end = farthest  # open new window

                if current_end >= n - 1:
                    break

        return jumps
