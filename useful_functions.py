# This function is used to force an integer/non-negative/number input etc
class Num_Imput:
    def __init__(self, question_text):
        self.question_text = question_text

    def ask(self):
        """Takes a question and forces a specific type of numerical input"""
        ans_temp = input(f'{self.question_text}: ')
        accept = False
        while not accept:
            try:
                # depending on the criteria, change the code below:
                ans = float(ans_temp)
                if ans > 0:
                    accept = True
                else:
                    ans_temp = input(f'Invalid input. {self.question_text}: ')
            except ValueError:
                ans_temp = input(f'Invalid input. {self.question_text}: ')

        return ans


# This is a function to force an Y or N answer
class Yes_No_Question:
    def __init__(self,question_text):
        self.question_text = question_text

    def ask(self):
        """Askes a question and forces a yes_or_no ans, returns 'y' or 'n' """
        while True:
            answer = str(input(f'{self.question_text} (y/n): '))
            if answer.lower() in ('y', 'n', 'yes', 'no'):
                break
            print("\ninvalid input.")

        if answer.lower() == 'y' or answer.lower() == 'yes':
            return 'y'
        else:
            return 'n'
