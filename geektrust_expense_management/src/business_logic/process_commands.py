from src.service.process_input import InputDifferentiate
from src.service.print_output import OutputPrint
class Process:

    def __init__(self):
        self.final_output = []
    def process_all_lines(self, lines):
        obj_input = InputDifferentiate()
        SPLIT_INITIAL_PART = 0
        # iterating for each line and processing the input commands of the input file
        for line in lines:
            line = line.split("\n")[SPLIT_INITIAL_PART]
            output = obj_input.process_line(line)

            if (isinstance(output, str)):
                self.final_output.append(output)
            else:
                # loop till each element in output
                for ele in output:
                    self.final_output.append(ele)

        obj_output = OutputPrint()
        # print all lines
        obj_output.print_lines(self.final_output)