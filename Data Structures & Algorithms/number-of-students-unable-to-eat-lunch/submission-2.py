class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Solution using queue structure
        n = len(students)
        q = deque(students)

        for s in sandwiches:
            cnt = 0
            # rearrange students if student and the sandwich does not match
            # until found a matched one or iterated all students
            while q[0] != s and cnt < n:
                print (q[0])
                cur = q.popleft()
                q.append(cur)
                cnt += 1

            # handle different while-break situation
            if s == q[0]:
                q.popleft()
                n -= 1
            else:
                break
        return n