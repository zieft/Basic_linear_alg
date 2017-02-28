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

    def plus(self, v):
        """
        Vector operation plus.
        结果 = 被加数 + 加数
        :self :实例化的向量，被加数
        :param v: the vector to be added on （加数)
        :return: the Vector of result.
        """
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        """
        Vector operation Subtraction.
        结果 = 被减数 - 减数
        :self: the vector from which another number is subtracted (被减数)
        :param v:the to be minused vector (减数)
        :return:result vector (结果)
        """
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        """
        scalar product of a vector.
        :param c: the scalar to be multiplied
        :return: the result vector
        """
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

## make a instance of a class Vector ##
my_vector = Vector([1, 2, 3])

## Vector Operations ##
v1 = Vector([8.218, -9.341])
v2 = Vector([-1.129, 2.111])
v1.plus(v2).__str__()
v3 = Vector([7.119, 8.215])
v4 = Vector([-8.223, 0.878])
v3.minus(v4).__str__()
v5 = Vector([1.671, -1.012, -0.318])
c = 7.41
v5.times_scalar(c).__str__()

