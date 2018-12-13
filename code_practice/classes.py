class person:
    def __init__(self, location, name, birthday):
        self.location = location
        self.name = name
        self.birthday = birthday

    def move_forward(self):
        self.location += 1


eli = person(2, "eli", "5-31-18")

print(eli)
