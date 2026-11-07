from collections import defaultdict
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        
        self.foods = {}
        self.foods_to_cuisine = {}
        self.cuisines = defaultdict(list)

        for i in range(len(foods)):
            self.foods[foods[i]] = ratings[i]
            self.foods_to_cuisine[foods[i]] = cuisines[i]
            self.cuisines[cuisines[i]].append((-ratings[i], foods[i]))

        for k in self.cuisines.keys():
            heapq.heapify(self.cuisines[k])

        # fruits: [(-5, apricot), (-3, apple)],
        # print(self.foods)
        # print(self.cuisines)
        return None
        pass
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foods_to_cuisine[food]
        
        self.cuisines[cuisine].remove((-self.foods[food], food))
        heapq.heapify(self.cuisines[cuisine])
        heapq.heappush(self.cuisines[cuisine], (-newRating, food))
        self.foods[food] = newRating
        return None
    def highestRated(self, cuisine: str) -> str:
        return self.cuisines[cuisine][0][1]
