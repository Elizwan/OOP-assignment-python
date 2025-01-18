# Base class
class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages

    def display_info(self):
        return f"'{self.title}' by {self.author}, Genre: {self.genre}, Pages: {self.pages}"

# Derived class (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, genre, pages, file_size, format):
        super().__init__(title, author, genre, pages)
        self.file_size = file_size
        self.format = format

    def display_info(self):
        return f"'{self.title}' by {self.author} (eBook), Genre: {self.genre}, Pages: {self.pages}, File Size: {self.file_size}MB, Format: {self.format}"

# Using the classes
paper_book = Book("2004", "Susan Shaw", "Fiction", 198)
ebook = EBook("Power of Thinking Big", "David Schwartz", "Self-Development", 318, 2, "PDF")

print(paper_book.display_info())
print(ebook.display_info())

#2
# Base class
class Vehicle:
    def move(self):
        pass  # Placeholder for polymorphic behavior

# Derived classes
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Using polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()  # Each class has its own implementation of move()
