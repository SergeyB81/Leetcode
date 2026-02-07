from typing import List
from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        size_to_people = defaultdict(list)

        result = []

        for person_id, group_size in enumerate(groupSizes):
            size_to_people[group_size].append(person_id)

        print(size_to_people)

        for group_size, people in size_to_people.items():
            for i in range(0, len(people), group_size):
                result.append(people[i:i+group_size])


        return result


if __name__ == '__main__':
    groupSizes = [3, 3, 3, 3, 3, 1, 3, 3]
    print(Solution().groupThePeople(groupSizes))