class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("Meow")


cat = Cat

cat.meow(1)