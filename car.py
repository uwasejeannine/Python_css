class Car:
      make="Toyota Prado"

      def __init__(self,model,registation,color,shape):
          self.model=model
          self.registation=registation
          self.color=color
          self.shape=shape
      def  move(self):
          return f"My car is from {self.module} with{self.registation} it's is{self.color} in shape is{self.shape} "

      def accelerated(self):
          return f"The car {self.module} with{self.registation} has bight color which is{self.color}  "

