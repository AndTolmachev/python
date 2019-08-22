def is_parallelogramm(a, b, c, d):
    def sqr_lenght(x, y):
        return (x[0] - y[0])**2 + (x[1] - y[1])**2
    side_1 = sqr_lenght(a, b)
    side_2 = sqr_lenght(a, c)
    side_3 = sqr_lenght(a, d)
    side_4 = sqr_lenght(b, d)
    side_5 = sqr_lenght(b, c)
    side_6 = sqr_lenght(c, d)
    if (side_1 == side_6 and side_2 == side_4 or
            side_3 == side_5 and side_4 == side_2 or
            side_1 == side_6 and side_3 == side_5):
        return True
    else:
        return False


z = is_parallelogramm((1, 1), (1, 4), (4, 1), (4, 4))
print(z)
