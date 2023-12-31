import math
class my_Calculator:
    def __init__(self,calculator_name):
        self.name = calculator_name
    #Le self correspond au instance et pas a la class (my_calculator)
    
    def introduce_my_self(self):
        print(f"Hey my name is {self.name} and i'll help you to make some calculations! Let's gooo!")

    def quadratic(self,a, b, c):
        """Solve the quadratic equation ax^2 + bx + c = 0. Returns two solutions as a tuple."""
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return None  # No real solutions
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    
    def Newton (self, m, b):
        F =  m * b
        print (f"The value of {m} multiplicated by {b} is equal to {F}")
    
    def Work (self, d, F, c): 
        W = F * d * c
        print (f"The Work for this calculus is equal too {W}")
    
    def Speed (self,d, t):
        v = d / t
        print (f"The speed is equal to {v}")
    
    def Kinetic_Energy (self, m, v, c):
        c = 0.5
        KE =  c* v**2 * m
        print (f"The Kinetic Energy is equal to {KE}")
