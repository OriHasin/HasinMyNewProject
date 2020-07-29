class Circle:
    #Radius,Pi
    def __init__(self,Radius):
        self.Radius=Radius
        self.Pi=3.14
    def area(self):
        return (self.Pi*self.Radius)**2
    def circumference(self):
        return 2*self.Pi*self.Radius
if __name__=='__main__':
    Radius=int(input("Enter a new radius: "))
    Circle1=Circle(Radius)
    print("The area of circle: "+str(Circle1.area())+" "+"The circumference of circle: "+str(Circle1.circumference()))