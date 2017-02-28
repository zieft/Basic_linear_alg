class Vector(object):
    def __init__(self, coordinates:list):
        """
        The initializer creates a VECTOR based on an input [LIST] of coordinates,
        and also set the dimensions of space the vector lives in.
        :param coordinates: should be a list
        """
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

my_vector = Vector([1, 2, 3])
