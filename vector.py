class Vector:

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        

    def __add__(self, another):
        return Vector(self.x + another.x, self.y + another.y, self.z + another.z)


    def __str__(self):
        return f"[{self.x}, {self.y}, {self.z}]"


    def len(self) -> int:
        """
            Length of vector
        """
        x, y, z = self.x, self.y, self.z
        return (x ** 2 + y ** 2 + z ** 2) ** 0.5
    

    def normalize(self):
        length = self.len()
        if length != 0:
            self.x /= length 
            self.y /= length 
            self.z /= length 


    def multiplyByScalar(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar


if __name__ == "__main__":
    vector = Vector(1, 1, 0)
    vector.normalize()
    print(vector)
