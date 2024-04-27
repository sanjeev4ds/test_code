class CalculateAmounts:
    # re-calculating for third member also
    def connected_amount(self, giver, receiver, remain):
        ABSOLUTE_ZERO = 0
        try:
            if ((self.giver_receiver[giver][receiver] > ABSOLUTE_ZERO) and (self.giver_receiver[receiver][remain] > ABSOLUTE_ZERO)):
                if (self.giver_receiver[receiver][remain] <= self.giver_receiver[giver][receiver]):
                    self.giver_receiver[giver][remain] += self.giver_receiver[receiver][remain]
                    self.giver_receiver[giver][receiver] -= self.giver_receiver[receiver][remain]
                    self.giver_receiver[receiver][remain] = ABSOLUTE_ZERO
                else:
                    self.giver_receiver[giver][remain] += self.giver_receiver[giver][receiver]
                    self.giver_receiver[receiver][remain] -= self.giver_receiver[giver][receiver]
                    self.giver_receiver[giver][receiver] = ABSOLUTE_ZERO
            return True
        except:
            return False

    # calcualte the ramaining amounts for every member
    def evaluate_amounts(self):
        COMPLETE_CUT = 0
        for giver in self.giver_receiver:
            for receiver in self.giver_receiver[giver]:
                if (self.giver_receiver[giver][receiver] >= self.giver_receiver[receiver][giver]):
                    self.giver_receiver[giver][receiver] -= self.giver_receiver[receiver][giver]
                    self.giver_receiver[receiver][giver] = COMPLETE_CUT
                else:
                    self.giver_receiver[receiver][giver] -= self.giver_receiver[giver][receiver]
                    self.giver_receiver[giver][receiver] = COMPLETE_CUT

                NUMBER_OF_RECEIVER = 2
                REMAIN_RECEIVER_INDEX = 0
                if (len(self.giver_receiver[giver]) == NUMBER_OF_RECEIVER):
                    remain = [ele for ele in list(self.giver_receiver[giver].keys()) if ele != receiver][REMAIN_RECEIVER_INDEX]
                    self.connected_amount(giver, receiver, remain)

    #calculate all the dues pending for member
    def calculate_dues(self, member):
        set_amount = set()
        amount_giver = {}
        for giver in self.giver_receiver:
            if giver != member:
                amount_due = self.giver_receiver[giver][member]
                if (amount_due not in amount_giver):
                    amount_giver[amount_due] = [giver]
                else:
                    amount_giver[amount_due].append(giver)

                amount_giver[amount_due].sort()
                set_amount.add(amount_due)
        list_amounts = list(set_amount)
        list_amounts.sort(reverse=True)
        return list_amounts, amount_giver

    def remaining_dues(self, member_name):
        ABSOLUTE_ZERO = 0
        check_find_issue = False
        for member in self.giver_receiver:
            if (member == member_name):
                for receiver in self.giver_receiver[member]:
                    if (self.giver_receiver[member][receiver] != ABSOLUTE_ZERO):
                        check_find_issue = True
                        return check_find_issue
            elif(self.giver_receiver[member][member_name] != ABSOLUTE_ZERO):
                check_find_issue = True
                return check_find_issue
        return check_find_issue