# A program that will save a phone number in a file and possibly also tells the country of the number later down the line
import os

phoneNumbers = []
x = len(phoneNumbers)
y = phoneNumbers

def contactInput():
    while True:
        n = input("- ")
        os.system("cls")
        c = input(": ")
        os.system("cls")
        cn = (c + " ") + (f"- {n}")
        phoneNumbers.append(cn) 
        if c == "q" or n == "q":
            del phoneNumbers[-1]
            return

def save():
    s = input("Save the list locally? (y/n)\n")
    if s == "y":
        with open("saved_numbers.txt", "a") as txt_file:
            for item in phoneNumbers:
                txt_file.write(f"{item}\n")

def main():
    contactInput()
    save()

print("First type the contact name, then type the phone number. To finish type 'q'")
main()