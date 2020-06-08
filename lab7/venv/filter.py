from abc import ABC, abstractmethod
from enum import Enum
import re
import sys


class Filter(ABC):
    @abstractmethod
    def name(self) -> str:
        """Provides a name of the rule (like FP005)."""
        pass

    @abstractmethod
    def matches(self, line: str) -> bool:
        """Returns True if a given line matches the filter, otherwise, returns False."""
        pass

class FP001(Filter):
    def name(self) -> str:
        return 'FP001'

    def matches(self, line: str) -> bool:
        return line.endswith('.')

class FP002(Filter):
    def name(self) -> str:
        return 'FP002'

    def matches(self, line: str) -> bool:
        return (len(line) > 0 and len(line) <= 100)

class FP003(Filter):
    def name(self) -> str:
        return 'FP003'

    def matches(self, line: str) -> bool:
        return line.count("a") >=5

class FN201(Filter):
    def name(self) -> str:
        return 'FN201'

    def matches(self, line: str) -> bool:
        return line.count("z") > 3

class FN202(Filter):
    def name(self) -> str:
        return 'FN202'

    def matches(self, line: str) -> bool:
        return len(line) == 0

class FN203(Filter):
    def name(self) -> str:
        return 'FN203'

    def matches(self, line: str) -> bool:
        return line.isalpha()

class Rules(Enum):
    FP001 = FP001()
    FP002 = FP002()
    FP003 = FP003()
    FN201 = FN201()
    FN202 = FN202()
    FN203 = FN203()

    @classmethod
    def rules_generator(cls):
        for item in cls:
            yield item.value

class Mode(ABC):
    @abstractmethod
    def filter_generator(self, file_line):
        line_generator= {}
        count_line = 0
        for line in file_line:
            count_line+=1
            str = " ".join([rule.name() for rule in Rules.rules_generator() if rule.matches(line)])
            line_generator [f'{count_line}'] = str
        return line_generator


    @staticmethod
    def get_mode(mode: str):
        """
        Method receives argument from command line: 'filter' or 'annotate' and creates the instance
        of corresponding Class which will contains method with requested logic.
        """
        if mode == 'filter':
            return FilterMode()
        elif mode == 'annotate':
            return AnnotateMode()
        else: raise Exception('Wrong arguments!')

class FilterMode(Mode):
    def filter_generator(self, file_line):
        """
        Method calls for parent method which is processing text file content and contains additional
        logic specific for 'filter' scenario: the program should display lines in console based on given
        rules.
        """
        file_rules = super().filter_generator(file_line)
        for key in file_rules.keys():
            if 'FP' in file_rules[key]:
                print(f'{key}:{(file_line[int(key) - 1]).strip()}')

class AnnotateMode(Mode):
    def filter_generator(self, file_line):
        """
        Method calls for parent method which is processing text file content and contains additional logic
        specific for 'annotate' scenario: the program has to display the information about which rules are
        applicable for each line.
        """
        file_rules = super().filter_generator(file_line)
        for key in file_rules.keys():
            print(f'{key}: {(file_rules[key]).strip()}')

if __name__ == '__main__':
    mode = Mode.get_mode(sys.argv[1])
    file_path = sys.argv[2]
    content = open(file_path, 'r')
    file_line = content.readlines()
    content.close()
    mode.filter_generator(file_line)