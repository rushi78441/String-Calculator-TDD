import re
from abc import ABC,abstractmethod

class NumberParser(ABC):
    """Abstract class for parsing strategy (Open-Closed Principle)"""
    @abstractmethod
    def parse(self,numbers : str) -> list[int]:
        pass


class DefaultNumberParser(NumberParser):
    """Concrete Parser : Single Responsibility"""
    
    def parse(self,numbers:str) -> list[int]:
        # Numbers in str
        working = numbers

        # handle_custom delimetrs
        if working.startswith("//"):
            delimeter_line,working = working[2:].split("\n",1)
            delimeter = delimeter_line.strip()
            working = working.replace(delimeter,",")
        
        # normalize new lines
        working = working.replace("\n",",")

        # Extract numbers
        num_list = []
        for num_str in working.split(","):
            striped = num_str.strip()
            if striped:
                num_list.append(int(striped))
        
        return num_list


class StringCalculatorKata:
    """Main Class : Following SOLID Principle"""
    def __init__(self, parser : NumberParser = None):
        self.parser = parser or DefaultNumberParser()

    def add(self, numbers : str) -> int:
        # Empty case
        if not numbers:
            return 0

        # num_list 
        num_list = self.parser.parse(numbers)

        # case : Negative numbers not allowed
        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"negatives not allowed : {', '.join(map(str,negatives))}")

        # case : numbers greater than 1000 ignored
        return sum(num for num in num_list if num < 1000)

calculater = StringCalculatorKata()
add = calculater.add