class Shoes:
    #створюємо клас 
    public_number = 0 # числове поле 
    public_string = "String" # стрічкове поле   
    def __init__(self, name="Default Name", price=0, size=0, colour="Unknown Colour"):
        #init - ініціалізація(налаштувати при створенні), надати початкові значення 
        #self - перший параметр ,який надає  доступ до атрибутів 
        #self - це параметр, що передає посилання на поточний об'єкт класу, дозволяючи взаємодіяти з його полями.
        # приватній поля 
        self.__name = name
        self.__price = price
        self.__size = size
        self.__colour = colour 
        # Додаткові публічні поля можуть змінюватися для кожного об'єкта
        Shoes.public_number += 1
        self.public_string = f"Example {Shoes.public_number}"
    # def info(self):
    #     return f"Shoes name: {self.__name}, Size: {self.__size}, Price: {self.__price} UAN, Colour:{self.__colour}."
        #повернути результат виконання методу

# example
# shoes1 = shoes("Nike",5000,42,"black")
# print(shoes1.info())
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_size(self):
        return self.__size

    def get_colour(self):
        return self.__colour        
    
    #створення для красивого читання
    def __str__(self):#print(shoes)  # Використає __str__(смикниться str)
                return (f"(str)Shoes: {self.__name}, Size: {self.__size}, Price: {self.__price} UAN"
                        f"Colour: {self.__colour}, Public Number: {Shoes.public_number}"
                        f" Public String: {self.public_string}")
    #створення для того як відновити об'єкт 

    def __repr__(self):#print(rerp(shoes))  # Використає __rerp__(смикнеться тільки тоді коли print(rerp(example)))
                return (f"(repr)Shoes: {self.__name}, Size: {self.__size}, Price: {self.__price} UAN"
                        f"Colour: {self.__colour}, Public Number: {Shoes.public_number}"
                        f" Public String: {self.public_string}")
    
    def __del__(self):#деструктор
        print(f"Shoes object '{self.__name}' is being deleted.")

def main():
    # #Функція main є корисним способом організації коду, покращення його структу   ри,
    # #  читабельності та управління його виконанням. 
    # # Це дозволяє програмістам легше працювати з кодом
    # # та повторно використовувати його та виконувати тестування.
        shoes1 = Shoes("Nike",5000,42,"black")
        shoes2 = Shoes("Rick Owens",40000,43,"black and white")
        shoes3 = Shoes("New Balance",8000,38,"red")

        # Виведення інформації про кожен об'єкт
        print(shoes1)
        print(repr(shoes1))
        print(shoes2)
        print(repr(shoes2))
        print(shoes3)
        print(repr(shoes3))

        # print(f"Public Number: {shoes.public_number}")
        # print(f"Public String (shoes1): {shoes1.public_string}")
        # print(f"Public String (shoes2): {shoes2.public_string}")
        # print(f"Public String (shoes3): {shoes3.public_string}")    


main()