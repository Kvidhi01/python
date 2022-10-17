print('welcome to quiz-o-ring')
answer=input('are you ready to play the quiz ? (yes/no):')
score=0
total_question=3
 

 if answer.lower()=='yes':
    answer=input('question 1: what is your favourite programming language')
    if answer.lower()=='python':
        score += 1
        print('correct')
        else:
            print('wrong answer')


    answer=input('question 2: what is your favourite colour')
    if answer.lower()=='blue':
        score += 1
        print('correct')
        else:
            print('wrong answer')

            
    answer=input('question 3: who is your light in darkness')
    if answer.lower()=='my angel':
        score += 1
        print('correct')
        else:
            print('wrong answer')

            print('thank you for playing this small quiz game, you attempted',score,"questions correctly")
            mark=(score/total_questions)*100
            print('marks obtained:',mark)
            print('BYE!')