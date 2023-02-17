from Question import Question
question_prompts=[
    "1.what is the colour of apple? \n(a)red \n(b)yellow\n(c)black\n\n",
    "2.what is the colour of banana? \n(a)red \n(b)yellow\n(c)black\n\n",
    "3.what is the colour of hair? \n(a)red\n (b)yellow\n(c)black\n\n"
]

questions = [
Question(question_prompts[0], "a"),
Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]


def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1

    print("you got "+ str(score) + "/" + str(len(questions)))
run_test(questions)