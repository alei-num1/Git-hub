def describe_pet(animal_type, pet_name):
    print("\n I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# 可以分别把实参存储到形参里，这样就算顺序错了也没事
describe_pet(animal_type='hamster', pet_name='cute_ai')
