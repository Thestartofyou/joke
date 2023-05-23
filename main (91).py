def interpret_joke(joke):
    response = input(joke + " Is this joke funny? (y/n): ")
    
    if response.lower() == "y" or response.lower() == "yes":
        print("Glad you found it funny!")
    else:
        print("Sorry if it didn't make you laugh. Maybe next time!")

# Example usage
joke = input("Enter a joke: ")
interpret_joke(joke)
