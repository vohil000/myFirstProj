import random
import json

print("Welcome to this Random Trivia Game!")
while True:
    num_quest = int(input("From 1 - 20, how many questions would you like? \n"))
    if 1 <= num_quest <= 20:
        break
    else:
        print("That is not an option. Please try again.")

with open("questions.json", "r") as file:
    content = file.read()
data = json.loads(content)

num = 1
score = 0
for x in range(num_quest):
    question_set = random.choice(data)
    question = question_set.get("question_txt")
    answer_list = question_set.get("options_txt")
    answer_list = random.sample(answer_list, 4)
    correct_answer = question_set.get("options_txt")[0]

    num_str = str(num)
    print("\nQUESTION #" + num_str)
    print(question)
    print("A) " + answer_list[0])
    print("B) " + answer_list[1])
    print("C) " + answer_list[2])
    print("D) " + answer_list[3])

    while True:
        user_answer = input("Answer here: ")
        user_answer.lower()
        if user_answer not in ["a", "b", "c", "d"]:
            print("Not an option. Please try again.")
        elif user_answer == "a":
            if answer_list[0] == correct_answer:
                score = score + 1
            break
        elif user_answer == "b":
            if answer_list[1] == correct_answer:
                score = score + 1
            break
        elif user_answer == "c":
            if answer_list[2] == correct_answer:
                score = score + 1
            break
        elif user_answer == "d":
            if answer_list[3] == correct_answer:
                score = score + 1
            break

    num = num + 1
    data.pop()
score = str(score)
num_quest = str(num_quest)
print(score + " out of " + num_quest)



#     question, list_answer = random.choice(list(QUESTIONS.items()))
#     correct_answer = list_answer[0]
#     num_str = str(num)
#     print("\nQuestion #" + num_str)
#     print(question)
#     randomize_answers = random.sample(list_answer, 4)
#     print("A) " + randomize_answers[0])
#     print("B) " + randomize_answers[1])
#     print("C) " + randomize_answers[2])
#     print("D) " + randomize_answers[3])
#     while True:
#         user_answer = input("Answer here: ")
#         user_answer.lower()
#         if user_answer not in ["a", "b", "c", "d"]:
#             print("Not an option. Please try again.")
#         elif user_answer == "a":
#             if randomize_answers[0] == correct_answer:
#                 score = score + 1
#             break
#         elif user_answer == "b":
#             if randomize_answers[1] == correct_answer:
#                 score = score + 1
#             break
#         elif user_answer == "c":
#             if randomize_answers[2] == correct_answer:
#                 score = score + 1
#             break
#         elif user_answer == "d":
#             if randomize_answers[3] == correct_answer:
#                 score = score + 1
#             break
#     num = num + 1
#     QUESTIONS.pop(question)
# score = str(score)
# num_quest = str(num_quest)
# print(score + " out of " + num_quest)