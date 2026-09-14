class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), reverse = True)
        time_list = []
        mono_stack = []

        for pos, spe in cars:
            time = (target - pos) / spe
            time_list.append(time)
        
        for i in time_list:
            if len(mono_stack) == 0:
                mono_stack.append(i)
                continue
            
            if not i <= mono_stack[-1]:
                mono_stack.append(i)
        
        return len(mono_stack)
                
            