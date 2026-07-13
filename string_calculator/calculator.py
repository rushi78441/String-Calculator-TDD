import re

def add(numbers : str) -> int:
    # case  : Empty string
    if not numbers:
        return 0
    
    # case : Adding two or more Numbers seperated with comma
    # case : Supporting new line as delimeter
    # case : Supporting Custom delimeter "//"
    # default delimeter are comma and new line
    delimeter = ",|\n"
    
    if numbers.startswith("//"):
        # Split the header line from the actual numbers
        # e.g., "//;\n1;2" becomes header="//;" and numbers="1;2"
        header,numbers = numbers.split("\n",1)

        # extract custom delimeter charactors after  "//"
        custom_delim = header[2:]

        # Use re.escape to safely handle special regex characters like * or +
        delimeter = re.escape(custom_delim)

    
    # Split the string using the regex delimiter pattern
    # This cleanly handles commas, newlines, OR your custom delimiter
    num_list = [int(num) for num in re.split(delimeter, numbers) if num.strip()]
    
    # case : Negative numbers not allowed
    negatives = [num for num in num_list if num < 0]
    if negatives:
        raise ValueError(f"negatives not allowed : {', '.join(map(str,negatives))}")


    return sum(num_list)