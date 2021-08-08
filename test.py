def test():
    print("function called")

if __name__ == "__main__":
    greetings = ["Hello", "Bonjour", "Hola"]

    for greeting in greetings:
        print(f"{greeting}, World!")
    test()