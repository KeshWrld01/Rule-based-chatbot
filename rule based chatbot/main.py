import re, random
from colorama import Fore, init
# Initialise colorama (autoreset ensures each print resets after use)
init(autoreset=True)

# Destination + joke data
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don’t programmers like nature? Too many bugs!",
    "My dad said the colours go to the doctor? Because it had a virus!",
    "Why do trees always get mistletoe? Because of all the saps in hot spots!"
]

# Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Provide travel recommendations (recursive if user rejects suggestions)
def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: You chose " + preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        user_reply = normalize_input(input(Fore.YELLOW + "You: "))
        if "yes" in user_reply or "okay" in user_reply or "sure" in user_reply:
            print(Fore.GREEN + "TravelBot: Awesome! Enjoy " + suggestion + "!")
        elif "no" in user_reply:
            print(Fore.RED + "TravelBot: Let's try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")

# Offer packing tips based on user's destination and duration
def show_help():
    packing_tips = [
        "Don't forget sunscreen!",
        "Bring chargers/adapters.",
        "Check the weather forecast."
    ]
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    for tip in packing_tips:
        print(Fore.GREEN + "- " + tip)

# Tell a travel joke
def tell_joke():
    print(Fore.YELLOW + "* TravelBot: " + random.choice(jokes))

# Display help info
def display_help():
    print(Fore.MAGENTA + "Hi! I can:")
    print(Fore.MAGENTA + "- Suggest travel spots (say 'recommend')")
    print(Fore.MAGENTA + "- Offer packing tips (say 'help')")
    print(Fore.MAGENTA + "- Tell a joke (say 'joke')")
    print(Fore.MAGENTA + "- Exit (type 'bye' or 'exit')")

# Chat loop
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "help" in user_input or "packing" in user_input:
            show_help()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.GREEN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")

if __name__ =="__main__":
    chat()
