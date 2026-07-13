def add(numbers : str) -> int:
    # case  : Empty string
    if not numbers:
        return 0
    
    # case : Adding two or more Numbers seperated with comma
    # case : Supporting new line as delimeter
    if "," or "\n" in numbers:
        # replace the newline with comma , to handle both 
        numbers = numbers.replace("\n",",")

        # split and get numbers in list
        num_list = [int(number) for number in numbers.split(sep = ',') if number.strip()]
        return sum(num_list)


    # case : Adding Single Number
    return int(numbers)