def hotdogs():
    people = int(input("How many people will be at the cookout?: "))
    dogs = int(input("How many hotdogs will each person get?: "))

    num_people = int(people)
    num_dogs = int(dogs)

    package_dogs = 10
    package_buns = 8
    needed_dogs = num_dogs * num_people
    needed_buns = num_people*num_dogs
    print(needed_dogs)
    print(needed_buns)

hotdogs()
    