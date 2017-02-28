from decimal import Decimal, getcontext
from math import sqrt, acos, pi


class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize zero vector!'
    getcontext().prec = 14  # for better numerical precision
    def __init__(self, coordinates:list):
        """
        The initializer creates a VECTOR based on an input [LIST] of coordinates,
        and also set the dimensions of space the vector lives in.
        :param coordinates: should be a list
        """
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])  # to ensure all coordinates are decimal object
                                                                         #  instead of floating point numbers or integers.
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
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        # number coming from outside should be treated as decimal.
        return Vector(new_coordinates)

    def magnitude(self):
        """
        Find the magnitude of a Vector.
        :return: The result scalar.
        """
        coordinates_square = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_square))

    def normalized(self):
        """
        Find the direction of a Vector.
        :return: a direction vector with a magnitude of 1.
        """
        try:
            magnitude = Decimal(self.magnitude())
            return self.times_scalar(Decimal(1.0)/magnitude)
            # number coming from outside should be treated as decimal.

        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot(self, v):
        """
        Find dot production of two vectors.
        :param v:
        :return: a scalar
        """
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        """
        Find the angle (smaller one) between two vectors in radians or degrees
        :param v:
        :param in_degrees:
        :return:
        """
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = acos(u1.dot(u2))

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector!')
            else:
                raise e

        if in_degrees:
            degrees_per_radian = 180 / pi
            return angle_in_radians * degrees_per_radian
        else:
            return angle_in_radians

    def is_orthogonal_to(self, v, tolerance=1e-10):
        """
        to see if the dot product of two vectors equals to 0.
        :param v:
        :param tolerance: due to precision issues
        :return:boolean (True of False)
        """
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v, tolerance=1e-4):
        """

        :param v:
        :return: boolean (True or False)
        """
        return (
            self.is_zero() or
            v.is_zero() or
            abs(self.angle_with(v)) < tolerance or
            abs(abs(self.angle_with(v)) - pi) < tolerance
        )

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance


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

## find the magnitude and the direction ##
v6 = Vector([8.813, -1.331, -6.247])
v6.magnitude().__str__()
v6.normalized().__str__()

## solve the dot product and find angle between two vectors ##
v7 = Vector([-5.955, -4.904, -1.874])
v8 = Vector([-4.496, -8.755, 7.103])
v7.dot(v8).__str__()
v7.angle_with(v8, in_degrees=False).__str__()

## checking for Parallelism and Orthogonality ##
v9 = Vector([-7.579, -7.88])
v10 = Vector([22.737, 23.64])
v9.is_orthogonal_to(v10)
abs(abs(acos(v9.normalized().dot(v10.normalized()))) - pi) < 1e-4

# return Decimal('-1.00000000000000012486519283418') 超出了acos()的定义域
# 因此将小数点后面保留的位数再次减少，以去掉bug
# 更改getcontext().prec = 10后，上式返回Decimal('-0.9999999999')，符合acos()的定义域
v9.is_parallel_to(v10)
