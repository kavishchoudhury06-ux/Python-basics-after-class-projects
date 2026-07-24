# Polymorphism

# class 1

class india:

    def captial(self):
        print("New Delhi")

    def language(self):
        print("many languages")

    def type(self):
        print("Developing Country")

class usa:

    def captial(self):
        print("Washington D.C")

    def language(self):
        print("English")

    def type(self):
        print("Developed Country")



# Common interface
countries = [india(), usa()]
for country in (countries):
    country.captial()
    country.language()
    country.type()