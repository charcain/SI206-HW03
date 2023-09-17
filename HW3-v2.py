# Your name: Charlies Cain 
# Your student id: 5385 9084 
# Your email: charcain@umcih.edu 
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.  
    # For this assignment I asked chatGPT to help me format the structure of the code as well as where to include self. methods since that part is still confusing to me. 
    # Additionally, I gave chatGPT some of the messy and ineffient code I had written asked it to re-write it in a way that was more comprehensible and efficeint. (code a reader can actually make sense of) 
    # When I gave chatGPT oem of my code that had manual indexing in it, it taught me this cool method called 'enumerate' which was so helpful that included it in my print_question_history function
                
  
import random

# Create the class CootieCatcher
# Arguments: self (the curent object)
    # A set of possible answers (a list), 
    # A set of four numbers in the range from 0-7 inclusive (a list),
    # A set of the remaining four numbers in the range from 0-7 inclusive that were not in the first list (a list) 
    # A question history list 
    # An answers history list 

class CootieCatcher:
    def __init__(self, answers, num1s, num2s):
        self.answers_list = answers
        self.num1_list = num1s
        self.num2_list = num2s
        self.questions_history_list = []
        self.answers_history_list = []

    # Create the __str__ method
    # Argument: self (the curent object)
    # Return: a string with all of the answers in the answers_list separated by commas

    def __str__(self):
        return ", ".join(self.answers_list)
    
# Create the ask method 
# Arguments: self (the curent object)
# A question (string)
# Return: An answer (string)

# The method takes a question and first checks if the question is already in the questions_history_list.
# If so, it returns a string, "I've already answered that question”
# Otherwise: 
#   It adds the question to the questions_history_list
#	Asks for the favorite color and if the length of the respose is even, use num1_list in the next step, else use num2_list. 
#   Prompts the user to “Pick a number - <numbers from appropriate list here>: “ 
#   Returns the answer from the get_fortune method.



    def ask(self, question):
        if question in self.questions_history_list:
            return "I've already answered that question."

        self.questions_history_list.append(question)
        color = input("What is your favorite color: ")
        if len(color) % 2 == 0:
            nums = self.num1_list
        else:
            nums = self.num2_list
        
        while True:
            try:
                pick = int(input(f"Pick a number - {nums}: "))
                if pick in nums:
                    fortune = self.get_fortune(nums, pick)
                    return f"{question} - {fortune}"
                else:
                    print("That number is not one you can choose! Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")


# Create the get_fortune method
# Argument: self (the curent object)
# nums (the number list that pick should be in)
# pick (the number the user entered)
# Return: an answer (string) 
# This method checks if pick is in nums and if not prints, “That number is not one you can choose! Please try again”.
# and asks for another number.
# if pick is in nums, it adds pick to the answers_history_list and returns the answer at that index from answers_list.

    def get_fortune(self, nums, pick):
        index = nums.index(pick)
        self.answers_history_list.append(self.answers_list[index])
        return self.answers_list[index]

# Create the print_question_history method
# Argument: self (the curent object)
# Return: None
#
# If there are no items in the questions_history_list, it prints "None yet"
# Otherwise, the method prints "<number> <question> - <answer>" for each of the values in the questions_history_list, each on a separate line.

    def print_questions_history_list(self):
        if not self.answers_history_list:
            print("None yet")
        else:
            for i, question in enumerate(self.questions_history_list):
                answer = self.answers_history_list[i]
                print(f"{i + 1}. {question} - {answer}")

def main():
    answers = [
        "Definitely", "Most likely", "It is certain", "Maybe",
        "Cannot predict now", "Very doubtful", "Don't count on it", "Absolutely not"]
    
    num1s = [0, 1, 2, 7]
    num2s = [3, 4, 5, 6]

    cootie_catcher = CootieCatcher(answers, num1s, num2s)

    while True:
        question = input("Enter a question (or 'quit' to exit): ")
        if question.lower() == 'quit':
            break
        response = cootie_catcher.ask(question)
        print(response)

    cootie_catcher.print_questions_history_list()


if __name__ == "__main__":
    main()  # Run the main function for user interaction

main()



