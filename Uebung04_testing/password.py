import string


def is_password_valid(password):
    digits = []
    capital_letters = []
    special_characters = []

    for character in password:
        if character.isdigit():
            digits.append(character)
        elif character.isupper():
            capital_letters.append(character)
        elif character in string.punctuation:
            special_characters.append(character)
        else:
            continue

    

   
    if len(password) < 8:
        return "password is not valid"
    
    elif len(digits) < 2:
        return "password needs at least 2 digits"

    elif len(capital_letters) < 1:
        return "password needs at least 1 capital letter"
    
    elif len(special_characters) < 1:
        return "password needs at least 1 special character"
    

    else:
        return "password is valid"


if __name__ == "__main__":
    print(is_password_valid("Wasserflasche12"))