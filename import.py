import re

def check_length(password):
    return len(password) >= 8

def check_character_variety(password):
    return re.search(r"[a-z]", password) and \
           re.search(r"[A-Z]", password) and \
           re.search(r"\d", password) and \
           re.search(r"[\W_]", password)

def check_common_words(password):
    common_words = ["password", "123456", "qwerty", "admin"]
    return password.lower() not in common_words

def check_sequential_characters(password):
    for i in range(len(password) - 2):
        if ord(password[i]) == ord(password[i+1]) - 1 == ord(password[i+2]) - 2:
            return False
    return True

def calculate_password_strength(password):
    strength = 0
    
    if check_length(password):
        strength += 1
    
    if check_character_variety(password):
        strength += 1
    
    if check_common_words(password):
        strength += 1
    
    if check_sequential_characters(password):
        strength += 1
    
    return strength

def get_strength_description(strength):
    if strength >= 4:
        return "Strong"
    elif strength >= 3:
        return "Moderate"
    else:
        return "Weak"

# Example usage
password = input("Enter a password: ")
strength = calculate_password_strength(password)
strength_description = get_strength_description(strength)
print(f"Password strength: {strength_description}")
