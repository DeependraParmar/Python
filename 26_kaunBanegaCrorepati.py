import time

questions = [
    "What is the capital city of France?",
    "Which planet is known as the Red Planet?",
    "Who wrote the play 'Romeo and Juliet'?",
    "In which year did World War II end?",
    "What is the largest mammal on Earth?",
    "Who is known as the 'Father of Computer Science'?",
    "What is the currency of Japan?",
    "Which element has the chemical symbol 'O'?",
    "What is the largest ocean on Earth?",
    "Who is the author of the Harry Potter book series?"
]
options = [
    ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
    ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"],
    ["a) William Shakespeare", "b) Jane Austen", "c) Charles Dickens", "d) Mark Twain"],
    ["a) 1942", "b) 1945", "c) 1950", "d) 1939"],
    ["a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Gorilla"],
    ["a) Alan Turing", "b) Bill Gates", "c) Steve Jobs", "d) Charles Babbage"],
    ["a) Yuan", "b) Won", "c) Yen", "d) Ringgit"],
    ["a) Oxygen", "b) Gold", "c) Iron", "d) Sodium"],
    ["a) Atlantic Ocean", "b) Indian Ocean", "c) Southern Ocean", "d) Pacific Ocean"],
    ["a) J.R.R. Tolkien", "b) J.K. Rowling", "c) George R.R. Martin", "d) Suzanne Collins"]
]
correct_answers = ["c", "b", "a", "b", "b", "a", "c", "a", "d", "b"]

prize_amounts = [10000, 20000, 50000, 100000, 200000, 400000, 800000, 1600000, 3200000, 6400000]

amount_won = 0

print("******* LET'S START KAUN BANEGA CROREPATI *********")
print()
print()
time.sleep(2)

for i in range(0,len(questions)):
    print(f"Ques {i+1}: ", questions[i], f"\t\t\t\t\t Price: {prize_amounts[i]}")
    print()

    option = options[i]
    for j in option:
        print(j)
    
    isCorrectFormat = False
    ans = 0
    while(isCorrectFormat == False):
        ans = input("Enter your ans(a/b/c/d): ")

        if(ans == 'a' or ans == 'b' or ans == 'c' or ans == 'd'):
            isCorrectFormat = True
        else:
            print("Invalid Format of ans...")
    
    
    if(ans == correct_answers[i]):
        amount_won = amount_won + prize_amounts[i]
        print()
        print(f"✅ Correct Answer....You won ₹{amount_won}")
    else:
        print(f"❌ Wrong Answer....You are taking ₹{amount_won} home")
        print(f"Correct Answer is: {correct_answers[i]}")
        print()
        break
    
    print()
    print()
    time.sleep(2)
    print(f"Next Question for ₹{prize_amounts[i+1]} in 5 seconds")
    time.sleep(5)
    print()
    
