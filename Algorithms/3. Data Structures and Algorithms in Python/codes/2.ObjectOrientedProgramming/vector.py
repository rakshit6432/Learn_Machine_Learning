class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, value):
        """Return sum of two vectors."""
        if len(self) != len(value):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + value[j]
        return result

    def __eq__(self, value):
        """Return True if vector has same coordinates as other."""
        return self._coords == value._coords

    def __ne__(self, value):
        """Return True if vector differs from other."""
        return not self == value

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'

    def __sub__(self, value):
        if len(self) != len(value):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - value[j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result


if __name__ == '__main__':

    v1 = Vector(5)
    v2 = Vector(5)
    for i in range(5):
        v1[i] = 5
        v2[i] = i

    print("Sum of \t\t{} and {}: \t{}".format(v1, v2, v1 + v2))
    print("Difference of \t{} and {}: \t{}".format(v1, v2, v1 - v2))
    print("Difference of \t{} and {}: \t{}".format(v2, v1, v2 - v1))
    print("Negative of \t{}: \t\t\t{}".format(v2, -v2))
