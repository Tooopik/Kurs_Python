def greet(name, message, separator=" "):
    print(message, name, sep=separator)


greet("Arek", "Witaj")
greet("Arek", "Witaj", "TEST")
greet(message="Arek", name="Witaj", separator="\n")
