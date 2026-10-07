class Person:

    # class attribute
    quality = "a good person"

    # instance attributes
    def __init__(self, name, age, school, religion, hobbies):
        self.name = name
        self.age = age
        self.school = school
        self.religion = religion
        self.hobbies = hobbies

# instantiate the Person class
izaad = Person(
    "Izaad",
    12,
    "AKAD",
    "Muslim",
    ["karate", "swimming", "football", "playing games", "arts"]
)

# access the class attribute
print("Izaad is {}".format(izaad.quality))

# access the instance attributes
print("{} is {} years old".format(izaad.name, izaad.age))
print("{} studies in {}".format(izaad.name, izaad.school))
print("{} is a {}".format(izaad.name, izaad.religion))
print("{} likes {}".format(izaad.name, ", ".join(izaad.hobbies)))