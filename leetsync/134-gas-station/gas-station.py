class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas is less than total cost, it's impossible
        if sum(gas) < sum(cost):
            return -1
        start_point, total_tank, length_of_loop = 0, 0, len(gas)
        for i in range(length_of_loop):
            total_tank += gas[i] - cost[i]
            # If we run out of gas at this station
            if total_tank < 0:
                # Pick the NEXT station as the new starting point
                start_point = i + 1
                # Reset our tank for the new start
                total_tank = 0
        return start_point