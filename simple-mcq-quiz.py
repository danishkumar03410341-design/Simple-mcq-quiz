print("Welcome to the Simple Quiz Game! ")
score = 0   

print("\n1. What is 2 + 2?")
print("A. 3")
print("B. 4")
print("C. 5")
print("D. 6")

answer = input("Your answer (A/B/C/D): ").upper()
if answer == "B":
    print("Correct! ")
    score += 1
else:
    print("Wrong!  The correct answer is B")
    
print("\n2. What is the Independence Day of Pakistan?")
print("A. 14 Aug")
print("B. 15 Aug")
print("C. 16 Aug")
print("D. 17 Aug")
answer = input("Your answer (A/B/C/D): ").upper()
if answer == "A":
    print("Correct! ")
    score += 1
else:
    print("Wrong!  The correct answer is A")

print("\n3. Who is the founder of Pakistan?")
print("A. Allama Iqbal")
print("B. Liaquat Ali Khan")
print("C. Muhammad Ali Jinnah")
print("D. Zia-ul-Haq")
answer = input("Your answer (A/B/C/D): ").upper()
if answer == "C":
    print("Correct! ")
    score += 1
else:
    print("Wrong!  The correct answer is C")

print("\n4. How many provinces are there in Pakistan?")
print("A. 4")
print("B. 5")
print("C. 6")
print("D. 3")
answer = input("Your answer (A/B/C/D): ").upper()
if answer == "A":
    print("Correct! ")
    score += 1
else:
    print("Wrong!  The correct answer is A")
    
print("\n5. Where is Mehran University located?")
print("A. Islamabad")
print("B. Karachi")
print("C. Jamshoro")
print("D. Lahore")
answer = input("Your answer (A/B/C/D): ").upper()
if answer == "C":
    print("Correct! ")
    score += 1
else:
    print("Wrong!  The correct answer is C")

print(f"\nYour score is {score}/5")

print("Thanks for playing! ")    

if score == 5:
    print("Excellent!  You got all answers correct!")
elif score >= 3:
    print("Good Job  Keep it up!")

