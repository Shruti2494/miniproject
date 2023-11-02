class Flower:
    def __init__(self, name, color, price, quantity):
        self.name = name
        self.color = color
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.color} {self.name} - ${self.price} ({self.quantity} available)"

class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower, quantity=1):
        for f in self.flowers:
            if f[0] == flower:
                f[1] += quantity
                return
        self.flowers.append([flower, quantity])

    def calculate_cost(self):
        total_cost = 0
        for flower, quantity in self.flowers:
            total_cost += flower.price * quantity
        return total_cost

    def __str__(self):
        bouquet_str = "Bouquet Contents:\n"
        for flower, quantity in self.flowers:
            bouquet_str += f"{flower.name} ({quantity})\n"
        bouquet_str += f"Total Cost: ${self.calculate_cost()}"
        return bouquet_str

class FlowerShop:
    def __init__(self):
        self.inventory = []

    def add_flower(self, flower):
        self.inventory.append(flower)

    def create_bouquet(self):
        bouquet = Bouquet()
        return bouquet

    def sell_bouquet(self, bouquet):
        for flower, quantity in bouquet.flowers:
            for item in self.inventory:
                if item == flower:
                    item.quantity -= quantity

    def check_inventory(self):
        for flower in self.inventory:
            if flower.quantity <= 5:
                print(f"Low stock alert: Only {flower.quantity} {flower.name} left. Consider ordering more.")

rose = Flower("Rose", "Red", 2.5, 20)
tulip = Flower("Tulip", "Yellow", 1.5, 15)
daisy = Flower("Daisy", "White", 1.0, 10)

flower_shop = FlowerShop()
flower_shop.add_flower(rose)
flower_shop.add_flower(tulip)
flower_shop.add_flower(daisy)

bouquet1 = flower_shop.create_bouquet()
bouquet1.add_flower(rose, 5)
bouquet1.add_flower(tulip, 7)

print(bouquet1)
flower_shop.sell_bouquet(bouquet1)

bouquet2 = flower_shop.create_bouquet()
bouquet2.add_flower(daisy, 3)
print(bouquet2)
flower_shop.sell_bouquet(bouquet2)

flower_shop.check_inventory()
