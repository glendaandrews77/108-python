# global var
from config import developer

# functions
def print_menu():
    print('hello  ')
    print('____PySoft 3000 ___')
    print('----------)')

def dictionary_1():
    pet = {
        "type": "rabbit",
        "name": "luna",
        "color": "white",
        "age": 2
    }

    print(pet)
    print("My pet is " + pet["name"])
    # modify
    pet["age"] = 3
    # add
    pet["size"] = "small"
    # remove
    pet.pop("type")
    print(pet)

def dictionary_2():
    print(developer)

    # 1 - print the first name like: first last
    print(developer["first"] + " " + developer["last"])

    # 2 - print the full address: street #, city
    address = developer["address"]
    print(address["street"] + " " + address["num"] + ", " + address["city"])

developer = {
    "first": "Gigi",
    "last": "Bailey",
    "age": "46",
    "email": "tx2vabch@gmail.com",
    "hobbies": ["code", "singing"],
    "address": {
        "num": "5048",
        "street": "holly farms",
        "city": "virgina beach"
    }
}


# plain instructions
# function calls
print_menu()
dictionary_1()
dictionary_2()
