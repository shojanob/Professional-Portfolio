# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"You live in {location}")
    print(f"{name}, How is it like in {location}?")
greet_with("Shoh", "Springfield")

# Functions with keyword arguments
greet_with(location= "Dushanbe", name="Shokhrukh")