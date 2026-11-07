from collections import defaultdict
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        
        self.foods = {}
        self.foods_to_cuisine = {}
        self.cuisines = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foods[food] = rating
            self.foods_to_cuisine[food] = cuisine
            self.cuisines[cuisine].append((-rating, food))

        for k in self.cuisines.keys():
            heapq.heapify(self.cuisines[k])

        # fruits: [(-5, apricot), (-3, apple)],
        # print(self.foods)
        # print(self.cuisines)
        return None
        
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foods_to_cuisine[food]
        heapq.heappush(self.cuisines[cuisine], (-newRating, food))
        self.foods[food] = newRating
        return None

    def highestRated(self, cuisine: str) -> str:
        while True:
            val, food = self.cuisines[cuisine][0]
            val = -val

            if self.foods[food] != val:
                heapq.heappop(self.cuisines[cuisine])
                continue

            return food
        
