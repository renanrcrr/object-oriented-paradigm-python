class P():
    def __init__(self, x):
        self.x = x
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        if x > 0:
            self._x = x

p = P(20)
print(p.x)
p.x = -5
print(p.x)