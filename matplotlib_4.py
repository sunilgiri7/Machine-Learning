# class bus():
#     def __init__(self,enginetype):
#         self.speed = 50
#         self.model = "Mahakali"
#         self.enginetype = enginetype
        
#     def drive(self,speed):
#         self.speed = speed
        
# class car(bus):
#     def __init__(self,engine):
#         super().__init__("car")
#         self.model = "Nano"
#         self.engine = engine
        
#     def drive(self, speed):
#         super().drive(speed)
#         self.speed = speed
#         print("driving my",self.enginetype, "car at", self.speed)
        
# car1 = bus("gas")
# car2 = car("liquid")

# print("engineType of my bus is",car1.enginetype)
# print("engine of my car start from",car2.engine)

# car1.drive(50)
# car2.drive(60)

thestr = "This is a string"
print(thestr)
thestr = 5