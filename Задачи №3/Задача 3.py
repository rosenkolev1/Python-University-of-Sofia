from re import X


def range_2d(coordsStart, coordsEnd):
    for x in range (coordsStart[0], coordsEnd[0]):
        for y in range(coordsStart[1], coordsEnd[1]):
            yield (x, y)

range_2d_generator = range_2d((1, 2), (3, 4))

print(next(range_2d_generator))
print(next(range_2d_generator))
print(next(range_2d_generator))
print(next(range_2d_generator))

