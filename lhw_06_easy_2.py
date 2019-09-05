def side_len(point_1, point_2) -> float:
    # вычисляет длинну отрезка по двум концам на координатной плоскости
    return (((point_1[0] - point_2[0]) ** 2
             + (point_1[1] - point_2[1]) ** 2) ** 0.5)


class IsoscelesTrapezium:
    def __init__(self, vertex_1, vertex_2, vertex_3, vertex_4):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.vertex_3 = vertex_3
        self.vertex_4 = vertex_4
        self.side_1 = side_len(vertex_2, vertex_1)
        self.side_2 = side_len(vertex_3, vertex_2)
        self.side_3 = side_len(vertex_4, vertex_3)
        self.side_4 = side_len(vertex_1, vertex_4)

    def is_isosceles_trapezium(self):
        diagonal_1 = side_len(self.vertex_1, self.vertex_3)
        diagonal_2 = side_len(self.vertex_2, self.vertex_4)
        if diagonal_1 == diagonal_2 \
                and self.side_1 != self.side_3 or self.vertex_2 == self.side_4:
            return True
        else:
            return False

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3 + self.side_4

    def square(self):
        # площадь
        a_1 = self.vertex_1[1] - self.vertex_3[1]
        b_1 = self.vertex_1[0] - self.vertex_3[1]
        a_2 = self.vertex_2[1] - self.vertex_4[1]
        b_2 = self.vertex_2[0] - self.vertex_4[0]
        # вычисляем значения a и b в ax + by + c для каждой из диагоналей
        sin = 1 - (a_1 * a_2 + b_1 * b_2) / ((a_1 ** 2 + b_1 ** 2) ** 0.5
                                             * (a_2 ** 2 + b_2 ** 2) ** 0.5)
        # вычисляем синус угла
        diagonal = side_len(self.vertex_1, self.vertex_3)
        return sin * diagonal ** 2 / 2
