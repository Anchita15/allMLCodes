from question import Question
question_prompts = [
    
    "What color are the apples?\n(a) Red/Green\n (b) Purple\n(c) Orange\n\n",
    "What color are the bananas?\n(a) Teal\n (b) Magenta\n(c) Yellow\n\n",
    "What color are the strawberries?\n(a) Yellow\n (b) Red\n"
                    ]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]

def run_test(questions): #this is the list of question objects that we want to ask the user 
    #once I am here I want to loop through each question, I want to ask the user, I want to get the user's answer and I want to check if its right. And we need to keep the track of how user does in test.

    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got" + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)

'''
What color are the apples?
(a) Red/Green
 (b) Purple
(c) Orange

a
What color are the bananas?
(a) Teal
 (b) Magenta
(c) Yellow

b
What color are the strawberries?
(a) Yellow
 (b) Red
b
You got2/3correct

'''