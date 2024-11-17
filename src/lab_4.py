class Shoes:
    public_number = 0 
    public_string = "String"   
    def __init__(self, name="Default Name", price=0, size=0, colour="Unknown Colour"):
        self.__name = name
        self.__price = price
        self.__size = size
        self.__colour = colour 
        Shoes.public_number += 1
        self.public_string = f"Example {Shoes.public_number}"

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_size(self):
        return self.__size

    def get_colour(self):
        return self.__colour        
    
    def __str__(self):
                return (f"(str)Shoes: {self.__name}, Size: {self.__size}, Price: {self.__price} UAN"
                        f"Colour: {self.__colour}, Public Number: {Shoes.public_number}"
                        f" Public String: {self.public_string}")

    def __repr__(self):
                return (f"(repr)Shoes: {self.__name}, Size: {self.__size}, Price: {self.__price} UAN"
                        f"Colour: {self.__colour}, Public Number: {Shoes.public_number}"
                        f" Public String: {self.public_string}")
    
    def __del__(self):
        print(f"Shoes object '{self.__name}' is being deleted.")

def main():
        slippers = Shoes("Nike",5000,42,"black")
        sneakers = Shoes("Rick Owens",40000,43,"black and white")
        sandals = Shoes("New Balance",8000,38,"red")

        print(slippers)
        print(repr(slippers))
        print(sneakers)
        print(repr(sneakers))
        print(sandals)
        print(repr(sandals))


main()