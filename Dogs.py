class Doggo():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Bork!")

    def bark2(self):
        print("Woof!")


my_doggo = Doggo("Kiara", "beagle")
print(my_doggo.name, "is a", my_doggo.breed, "!")
my_doggo.bark()

gfs_doggo = Doggo("Sky", "yorkshire")
print(gfs_doggo.name, "is a", gfs_doggo.breed, "!")
gfs_doggo.bark2()