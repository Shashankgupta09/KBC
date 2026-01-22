import sys
questions = [
    {
        "q": "Who is the president of the United States?",
        "options": [ "Joe Biden", "Donald Trump", "Barack Obama", "George W. Bush"],
        "answer": "Donald Trump"
    },
    {
        "q": "What is the capital of France?",
        "options": [ "Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "q": "Which planet is known as the Red Planet?",
        "options": [ "Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "q": "What is the largest mammal in the world?",
        "options": [ "Elephant", "Blue Whale", "Giraffe", "Great White Shark"],
        "answer": "Blue Whale"
    },
    {
        "q": "Who wrote 'Romeo and Juliet'?",
        "options": [ "Mark Twain", "Charles Dickens", "William Shakespeare", "Jane Austen"],
        "answer": "William Shakespeare"
    },
    {
        "q": "What is the chemical symbol for gold?",
        "options": [ "Au", "Ag", "Fe", "Pb"],
        "answer": "Au"
    },
    {
        "q": "Which country hosted the 2016 Summer Olympics?",
        "options": [ "China", "Brazil", "UK", "Russia"],
        "answer": "Brazil"
    },

]
levels = [1000, 5000, 10000, 50000, 100000, 200000, 500000, 1000000]
money = 0

i = 0
for i in range(len(questions)):
    print(f"Question for Rs.{levels[i]}:")
    print(questions[i]['q'])
    print(f"a. {questions[i]['options'][0]}")
    print(f"b. {questions[i]['options'][1]}")
    print(f"c. {questions[i]['options'][2]}")
    print(f"d. {questions[i]['options'][3]}")
    answer = input("Enter your answer (a/b/c/d): ").strip().lower()
    option_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
    if option_map.get(answer) is None:
        print("Invalid option. Exiting the game.")
        sys.exit()
    selected_option = questions[i]['options'][option_map[answer]]
    if selected_option == questions[i]['answer']:
        print(f"Correct! You have won Rs.{levels[i]}.\n")
    elif ( i == 0 and selected_option != questions[i]['answer']):
        print("Incorrect answer. You have won Rs.0. Game over.")
        sys.exit()
    elif(i == 4,5 and selected_option != questions[i]['answer']):
        print("Incorrect answer. You have won Rs.10000. Game over.")
        sys.exit()
    elif(i == 7 and selected_option != questions[i]['answer']):
        print("Incorrect answer. You have won Rs.500000. Game over.")
        sys.exit()
    else:
        print("Incorrect answer. Game over.")
        sys.exit()
print("Congratulations! You have answered all questions correctly and won the game.")
