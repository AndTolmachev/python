class Triangle:
    def __init__(self, vertex_1, vertex_2, vertex_3):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.vertex_3 = vertex_3
        self.side_1 = (((self.vertex_1[0] - self.vertex_2[0]) ** 2
                        + (self.vertex_1[1] - self.vertex_2[1]) ** 2) ** 0.5)
        self.side_2 = (((self.vertex_3[0] - self.vertex_2[0]) ** 2
                        + (self.vertex_3[1] - self.vertex_2[1]) ** 2) ** 0.5)
        self.side_3 = (((self.vertex_1[0] - self.vertex_3[0]) ** 2
                        + (self.vertex_1[1] - self.vertex_3[1]) ** 2) ** 0.5)

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def square(self):
        p = self.perimeter() / 2
        return (p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3)) ** 0.5

    def height(self):
        return 2 * self.square() / self.side_1

a = Triangle((0, 0), (3, 0), (0, 4))
print(a.square(), a.perimeter(), a.height())
