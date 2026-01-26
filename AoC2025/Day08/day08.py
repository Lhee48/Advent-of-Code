from pathlib import Path
from itertools import combinations
from collections import defaultdict


class UnionFind:
    def __init__(self, length):
        self.parent = {i: i for i in range(length)}

    def __str__(self):
        toret = ""
        for key, value in self.parent.items():
            toret += f"{key}: {value}\n"
        return toret

    def find(self, x) -> int:
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, i, j) -> None:
        self.parent[self.find(i)] = self.find(j)


def read_file(file_name: Path) -> list[tuple[int, int, int]]:
    path = Path(file_name)
    points = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file.readlines():
                x, y, z = (int(k) for k in line.split(","))
                points.append((x,y,z))
        return points
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: {path} not found")


def get_distance(pointA: tuple[int, int, int], pointB: tuple[int, int, int]) -> tuple[int, int]:
    Ax, Ay, Az = pointA
    Bx, By, Bz = pointB
    distance = (Ax-Bx)**2 + (Ay-By)**2 + (Az-Bz)**2
    return (distance, Ax)


def main() -> None:
    here = Path(__file__).parent
    file_name = here / "input"
    # file_name = here / "test"
    points = read_file(file_name)
    distances = []
    for i, pointA in enumerate(points):
        for j, pointB in enumerate(points):
            distance = get_distance(pointA, pointB)
            if i > j:
                distances.append((distance, i, j))

    distances_sorted = sorted(distances)
    UF = UnionFind(len(points))
    connections = 0
    for t, (_d, i, j) in enumerate(distances_sorted):
        if t == 1000:
            SZ = defaultdict(int)
            for x in range(len(points)):
                SZ[UF.find(x)] += 1
            sorted_SF = sorted(SZ.values())
            print("part 1", sorted_SF[-1]*sorted_SF[-2]*sorted_SF[-3])
        if UF.find(i) != UF.find(j):
            connections += 1
            if connections == len(points)-1:
                print("part 2", points[i][0] * points[j][0])
            UF.union(i,j)

    
if __name__ == "__main__":
    main()
