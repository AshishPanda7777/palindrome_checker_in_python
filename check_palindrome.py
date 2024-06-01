def is_palindrome(word):
    word = word.lower()  # Convert to lowercase for case-insensitivity
    return word == word[::-1]

def main():
    word = input("Enter a word: ")
    if is_palindrome(word):
        print("It's a palindrome!")
    else:
        print("It's not a palindrome.")
