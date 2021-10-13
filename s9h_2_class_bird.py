class Bird():
    def __init__(self,speicies,color,food,flight_altitude):
        self.speicies = speicies
        self.color = color
        self.food = food
        self.flight_altitude = flight_altitude
    def __str__(self):
        return f"this is a {self.color} {self.speicies} and its {self.food}"
    def ertefa(self):
        if self.flight_altitude <= 800:
            self.flight_altitude += 400
            print(f"{self.speicies} ba ertefa {self.flight_altitude} parvaz mikonad")
        else:
            print("golden eagle maxx flight altitude is 1200 meter")

bird = Bird("golden eagle","dark brown","carnivorous",0)
print(bird)
bird.ertefa()
bird.ertefa()
bird.ertefa()
bird.ertefa()
