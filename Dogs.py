class Doggo():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        return

    def bark(self):
        print("Bork!")
        return

    def bark2(self):
        print("Woof!")
        return


my_doggo = Doggo("Kiara", "beagle")
print(my_doggo.name, "is a", my_doggo.breed, "!")
my_doggo.bark()

gfs_doggo = Doggo("Sky", "yorkshire")
print(gfs_doggo.name, "is a", gfs_doggo.breed, "!")
gfs_doggo.bark2()
