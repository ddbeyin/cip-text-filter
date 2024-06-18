import os

def welcome():
    print("Welcome to the Customizable Text Filter Console Application!")
    print("Let's get started!")

def load_blacklist(blacklist_file):
    """Loads the blacklisted words from the specified file."""
    if not os.path.exists(blacklist_file):
        print(f"Error: Blacklist file '{blacklist_file}' not found.")
        return []
    with open(blacklist_file, "r") as f:
        return [word.strip().lower() for word in f]  # Lowercase for case-insensitive filtering

def get_target_text():
    """Prompts the user for the text to filter."""
    print("Please enter the text you want to filter (or type 'file' to load from a file):")
    choice = input()
    if choice.lower() == "file":
        while True:
            file_path = input("Enter the file path: ")
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    return f.read()
            else:
                print("File not found. Please try again.")
    else:
        return choice

def censor_text(text, blacklist):
    """Replaces blacklisted words with asterisks."""
    censored_text = text
    for word in blacklist:
        censored_text = censored_text.replace(word, "*" * len(word)) 
    return censored_text

def main():
    welcome()

    while True:
        blacklist_file = input("Enter the path to your blacklist file (or type 'exit' to quit): ")
        if blacklist_file.lower() == "exit":
            break
        
        blacklist = load_blacklist(blacklist_file)

        target_text = get_target_text()

        censored_text = censor_text(target_text, blacklist)
        print("Censored Text:")
        print(censored_text)

if __name__ == "__main__":
    main()

