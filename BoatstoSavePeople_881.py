#link https://leetcode.com/problems/boats-to-save-people/
class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()

        left = 0
        right = len(people)-1

        boats_number = 0

        while(left<=right):
            if(left==right):
                boats_number+=1
                break
            if(people[left]+people[right]<=limit):
                left+=1

            right-=1
            boats_number+=1
        return boats_number