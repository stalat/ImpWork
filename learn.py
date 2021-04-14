# Importing core python modules
import csv
import time
from random import randint

class LearnTable(object):
    def __init__(self):
        # User can chose any option out of these choices to make sure if he 
        # wish to learn further
        self.choices_to_make = ['y', 'Y', 'n', 'N']
        
        # Initialising User object with his name
        self.name = input("What's your name? - ")
        print("Hello, {0}! Your MindHouse session has been created!".format(self.name))
        print("\n")

        # initialising the CSV file-name with Users name
        self.filename = "{0}.csv".format(self.name)

        # initializing a list that'll maintain logs
        self.student_log = list()

    def get_questions(self):
        """
        return question & answer to the question
        """
        # Using random module to get numbers between 12 & 10 to learn tables till 12
        x, y = randint(1, 12), randint(1, 10)
        return str(x*y), str(x) + ' * ' + str(y)

    def log_to_file(self, **kwargs):
        """
        function to write logs into CSV file
        """
        # file will be created with these as headers
        fields = ["Question", "Answer", "IsCorrect", "TimeTaken"]

        with open(self.filename, 'w') as csvfile:
            # writing the logs into CSV file
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(self.student_log)


    def ask_question(self, proceed_to_play='Y'):
        """
        Prompt to User if he wishes to continue to learn
        """
        log_dict = dict()
        
        # getting the question to ask
        answer, question_to_ask = self.get_questions()

        # logging the start-time & end-time
        start = time.time()
        print("What is the answer of {0}?".format(question_to_ask))
        user_answer = input("Enter Answer? ".format(question_to_ask))
        end = time.time()

        # Here, we're checking if answer given is correct or wrong
        if user_answer != answer:
            print("Oops That's wrong\n")
            log_dict["IsCorrect"] = "No"
        else:
            print("Correct Answer\n")
            log_dict["IsCorrect"] = "Yes"
        
        log_dict['Question'] = question_to_ask
        log_dict['Answer']  = user_answer  
        log_dict["TimeTaken"] = '{0:.2f}'.format(end-start)
        self.student_log.append(log_dict)

        # capturing the logs with required details
        self.log_to_file()

        # User will keep on playing till he choses Y/y to the learning model
        # The loop will keep on going unless User presses n/N to learning model
        while proceed_to_play in ['y', 'Y'] or proceed_to_play not in self.choices_to_make:
            proceed_to_play = input("Want to play more?. Y/N - ")
            print("\n")
            if proceed_to_play not in self.choices_to_make:
                print("Looks like You've not chosen correct option, Please chose the correct optionhbjh")
                continue
            if proceed_to_play in ['y', 'Y']:
                return self.ask_question()

        print("Good Bye, {0}".format(self.name))

print("Hello, Welcome to Math practice program\n")
# Initialising the Learning model object
user_object = LearnTable()

# calling function that will perform required actions
user_object.ask_question()
