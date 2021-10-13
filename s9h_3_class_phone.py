class Phone():
    def __init__(self,brand,model,processor,pixel_size):
        self.brand = brand
        self.model = model
        self.processor = processor
        self.pixel_size = pixel_size
    def sim_card(self):
        print("taghir sim card")
    def ring(self,ring_number):
        print("ring" * ring_number)
    def __str__(self):
        return "this is a {} {} with {}  and {} pixel size".format(self.brand,self.model,self.processor,self.pixel_size)
phone = Phone("Samsung","Galaxy s9","snapdragon 845 processor","1440 * 2960")
print(phone)
phone.sim_card()
phone.ring(3)
