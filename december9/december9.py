class Blizzard:
    def __init__(self, x, y, f, b):
        self.x = x
        self.y = y
        self.f = f
        self.b = b
        self.day = 0

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(x={self.x}, y={self.y}, f={self.f}, b={self.b})"
        )

    @property
    def duration(self):
        return self.day - self.b

    def strength(self, distance):
        if self.duration < 0:
            # Blizzard haven't started
            return 0

        return max(self.f - self.duration - distance, 0)

    def distance(self, x, y):
        dx = abs(x - self.x)
        dy = abs(y - self.y)

        return dx + dy

    def __call__(self, x, y):
        return self.strength(self.distance(x, y))


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.snow_level = 0

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    def forecast(self, blizzards):
        self.snow_level = max(self.snow_level - 1, 0)
        todays_contribution = sum([blizzard(self.x, self.y) for blizzard in blizzards])
        self.snow_level += todays_contribution
        return str(self.snow_level)


if __name__ == "__main__":
    D, N, S = map(int, input().strip().split(" "))
    cells_of_interest = []
    for _ in range(N):
        cells_of_interest.append(Cell(*map(int, input().strip().split(" "))))
    blizzards = []
    for _ in range(S):
        blizzards.append(Blizzard(*map(int, input().strip().split(" "))))

    for day in range(1, D + 1):
        for blizzard in blizzards:
            blizzard.day = day
        forecast = [c.forecast(blizzards) for c in cells_of_interest]
        print(" ".join(forecast))
