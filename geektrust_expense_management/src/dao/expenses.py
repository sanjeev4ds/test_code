from src.service.calculate_amount import CalculateAmounts
from src.service.operation_member import OperationsMember
class Expenses(CalculateAmounts, OperationsMember):
    def __init__(self):
        self.giver_receiver = {}
    def move_in(self, input_line):
        MEMBER_INDEX = 1
        member_name = input_line.split(" ")[MEMBER_INDEX]
        MAX_ALLOWED_MEMBERS = 3
        if( (len(self.giver_receiver) < MAX_ALLOWED_MEMBERS) and (member_name not in self.giver_receiver)):
            self.giver_receiver[member_name] = {}
            super().add_new_member()
            return "SUCCESS"
        else:
            return "HOUSEFUL"
    def spend(self, input_line):
        words = input_line.split(" ")
        AMOUNT_INDEX = 1
        amount = int(words[AMOUNT_INDEX])
        GIVER_INDEX = 2
        giver = words[GIVER_INDEX]
        RECEIVER_START_INDEX = 3
        MEMBERS_COUNT = len(words[RECEIVER_START_INDEX:])
        NUMBER_OF_MEMBERS_SHARED = MEMBERS_COUNT + 1
        RECEIVERS_START_INDEX = 3

        # check if member not exist
        for member_name in  words[RECEIVERS_START_INDEX:]:
            if (member_name not in self.giver_receiver):
                return "MEMBER_NOT_FOUND"

        each_spends = amount // NUMBER_OF_MEMBERS_SHARED
        for index in range(MEMBERS_COUNT):
            member_name = words[RECEIVERS_START_INDEX + index]
            if (member_name in self.giver_receiver[giver]):
                self.giver_receiver[giver][member_name] += each_spends
            else:
                self.giver_receiver[giver][member_name] = each_spends
        # to evaluate all the dues at time of each spend for all the active members
        super().evaluate_amounts()
        return "SUCCESS"
    def dues(self, input_line):
        person_amount = []
        MEMBER_INDEX = 1
        member = input_line.split(" ")[MEMBER_INDEX]
        if (member in self.giver_receiver):
            list_amounts, amount_giver = super().calculate_dues(member)
            for amount in list_amounts:
                for amount_member in amount_giver[amount]:
                    string_member_amount = amount_member + " " + str(amount)
                    person_amount.append(string_member_amount)
            return person_amount
        else:
            return "MEMBER_NOT_FOUND"
    def clear_due(self, input_line):
        split_input_line = input_line.split(" ")
        GIVER_INDEX = 1
        giver = split_input_line[GIVER_INDEX]
        RECEIVER_INDEX = 2
        receiver = split_input_line[RECEIVER_INDEX]
        AMOUNT_INDEX = 3
        amount = int(split_input_line[AMOUNT_INDEX])
        if ((giver not in self.giver_receiver) or (receiver not in self.giver_receiver)):
            return "MEMBER_NOT_FOUND"
        elif (self.giver_receiver[receiver][giver] >= amount):
            self.giver_receiver[giver][receiver] += amount
            # evaluate all the dues at time of each spend for all the active members
            super().evaluate_amounts()
            return str(self.giver_receiver[receiver][giver])
        else:
            return "INCORRECT_PAYMENT"

    def move_out(self, input_line):
        input_line_split = input_line.split(" ")
        MEMBER_INDEX = 1
        member_name = input_line_split[MEMBER_INDEX]

        if (member_name not in self.giver_receiver.keys()):
            return "MEMBER_NOT_FOUND"
        else:
            check_find_issue = super().remaining_dues(member_name)
            if (check_find_issue == False):
                # remove the member from final dict
                super().remove_member(member_name)
                return "SUCCESS"
            else:
                return "FAILURE"