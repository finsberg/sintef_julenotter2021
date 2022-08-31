class Blizzard:
    def __init__(self, x, y, f, b):
        self.x = x
        self.y = y
        self.f = f
        self.b = b

    def __call__(self, x, y, day):

        if day - self.b < 0:
            return 0

        distance = abs(x - self.x) + abs(y - self.y)
        return max(self.f - day + self.b - distance, 0)


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.snow_level = 0

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    def forecast(self, blizzards, day):
        self.snow_level = max(self.snow_level - 1, 0)
        self.snow_level += sum(
            [blizzard(self.x, self.y, day) for blizzard in blizzards]
        )
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
        forecast = [c.forecast(blizzards, day) for c in cells_of_interest]
        print(" ".join(forecast))
