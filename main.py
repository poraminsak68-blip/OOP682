class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def info(seft):
    print(f"{seft.name}is{seft.age}years old.")

def __str__(seft):
    return f"{set.name}is{set.age}years old."   

def main():
    my_dog = Dog("Buddy",3)
    your_dod = Dog("paylie",2)
    print(my_dog)

if __name__ == "__main__":
    main()
