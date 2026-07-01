questions = [
    ["Who is Elon Musk", "Actor", "Entrepreneur", "Footballer", 2],
    ["What is Python", "Snake", "Programming Language", "Car Brand", 2],
    ["Who founded Microsoft", "Steve Jobs", "Bill Gates", "Elon Musk", 2],
    ["What does CPU stand for", "Central Power Unit", "Central Processing Unit", "Computer Personal Unit", 2],
    ["Who is the CEO of Tesla", "Jeff Bezos", "Elon Musk", "Mark Zuckerberg", 2],
    ["What is HTML used for", "Styling", "Database", "Web Structure", 3],
    ["Which one is an OS", "Python", "Windows", "HTML", 2],
    ["What does RAM stand for", "Random Access Memory", "Read Access Memory", "Rapid Action Module", 1],
    ["Who created Facebook", "Mark Zuckerberg", "Larry Page", "Sundar Pichai", 1],
    ["What is Git", "Text Editor", "Version Control System", "Operating System", 2],
    ["Which language is used for AI", "Python", "HTML", "CSS", 1],
    ["What is SQL used for", "Design", "Database", "Gaming", 2],
    ["Who invented the computer", "Charles Babbage", "Alan Turing", "Bill Gates", 1],
    ["What does API stand for", "Application Programming Interface", "Advanced Program Input", "Applied Protocol Interface", 1],
    ["Which one is a database", "Django", "MySQL", "Flask", 2],
    ["What is Linux", "Programming Language", "Operating System", "Browser", 2],
    ["Who owns Google", "Microsoft", "Alphabet", "Amazon", 2],
    ["What is Flask", "Database", "Web Framework", "Operating System", 2],
    ["Which one is a cloud service", "AWS", "Python", "Ubuntu", 1],
    ["What does OOP stand for", "Object Oriented Programming", "Only One Process", "Open Operation Protocol", 1]
]

prizes = [1000,2000,3000,5000,8000,12000,20000,35000,50000,75000,100000,150000,200000,300000,500000,750000,1000000,2000000,3500000,5000000]
i = 0

for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")

    # check whether the answer is correct or not
    a = int(input("Enter the answer 1 for a, 2 for b, 3 for c: "))

    if (question[4] == a):
        print("Correct Answer")
    else:
        print(f'Incorrect Answer. The Correct Answer is {question[4]}')
        print("Better Luck Next Time. ")
        break

    print(f"You won {prizes[i]}")
    i+=1