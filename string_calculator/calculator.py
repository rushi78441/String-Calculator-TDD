def add(numbers : str) -> int:
    # case  : Empty string
    if not numbers:
        return 0
    
    # case : Adding two or more Numbers seperated with comma
    if "," in numbers:
        total_sum = sum(int(number) for number in numbers.split(','))
        return total_sum

    # case : Adding Single Number
    return int(numbers)