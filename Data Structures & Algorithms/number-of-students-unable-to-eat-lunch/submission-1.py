class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # First Thought:
        #       Students is a circular queue
        #       Sandwiches is a stack
        # Key problem: 
        #       what is the judgment condition of all left students in the queue
        #       are unable to eat?
        # Crux:
        #       Because students are being repeatedly checking whether 
        #       they matched the top sandwiches in the sandwich stack,
        #       the real matter thing is:
        #       whether the numbers of same type of sandwiches and students matched,
        #       instead of the order of them
        # Pattern:
        #       a counter is needed for counting how many things of same type there are
        res = len(students)
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s] > 0:
                cnt[s] -= 1
                res -= 1
            else:
                return res

        return res