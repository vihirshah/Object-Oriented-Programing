class Color_shop(): # function to set the specific values 
    def set_color_cost(self,colour,cost):
        self.colour=colour
        self.cost=cost


    def show_colour_cost(self): # function to print the values 
        print(self.colour,self.cost)

p1=Color_shop()

p1.set_color_cost('red',500) # assigning the values 
p1.show_colour_cost()  # printing the values 