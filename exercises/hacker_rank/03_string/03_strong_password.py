
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
        
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    result = {"numbers": 0, "lower_case": 0, "upper_case": 0, "special_characters": 0}
    
    for p in password:
        if p in numbers:
            result["numbers"] += 1
        if p in lower_case:
            result["lower_case"] += 1
        if p in upper_case:
            result["upper_case"] += 1
        if p in special_characters:
            result["special_characters"] += 1
    
    count = 0
    
    if result["numbers"] == 0:
        count += 1
    if result["lower_case"] == 0:
        count += 1
    if result["upper_case"] == 0:
        count += 1
    if result["special_characters"] == 0:
        count += 1   
    
    is_big = n < 6   

    if count == 0 and is_big:
        return 6 - n
    elif count and is_big:
        quantos_faltam = 6 - n
        if count >= quantos_faltam:
            return count
        else:
            return quantos_faltam   
    elif is_big:
        return 6 - n
    return count


result = minimumNumber(4, '4700')
print(result)
assert result == 3