# by Kami Bigdely
# Extract class
class Person:
    def __init__(self, first_name, last_name, birth_year, email, movies_played):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.email = email
        self.movies_played = movies_played

    def send_hiring_email(self):
        print("email sent to: ", self.email)

    def print_name(self):
        print(self.first_name, self.last_name)
    
    def print_movies(self):
        for m in self.movies_played:
            print(m, end=', ')


movies1 = ['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby']
person1 = Person('elizabeth', 'debicki', 1990, 'deb@makeschool.com', movies1)

movies2 = ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']
person2 = Person('Jim', 'Carrey', 1962, 'jim@makeschool.com', movies2)
    

for person in [person1, person2]:
    person.print_name()
    person.print_movies()
    person.send_hiring_email()