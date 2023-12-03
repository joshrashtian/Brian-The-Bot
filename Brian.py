import json
import re
from difflib import get_close_matches

def loadBrain(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def saveBrain(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def findMatch(userQuestion: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(userQuestion, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def getAnswer(question: str, brain: dict) -> str | None:
    for q in brain["questions"]:
        if q["question"] == question:
            return q["response"]
        
def solveProblem(question: str) -> str | None:
    return str([int(s) for s in question.split() if s.isdigit()])
    

        
def Brian():
    brain: dict = loadBrain('brain.json')

    while True:
        userQuestion: str = input("You: ")

        if userQuestion.lower() == 'exit':
            break
        
        elif userQuestion.lower() == 'math':
            print("Brian: Riddle Me What?")

            problem: str = input('You: ')

            if problem.lower() == 'stop':
                break
            else:
                bestResult: str | None = solveProblem
                
                if bestResult:
                    print("Brian: " + str(bestResult))
                
                else:
                    print("Brian: Oops! Sadly, I could not figure it out.")
            

        else:
            bestResult: str | None = findMatch(userQuestion, [question["question"] for question in brain["questions"]])

            if bestResult:
                answer: str = getAnswer(bestResult, brain)
                print("Brian: " + str(answer))

            else:
                print("I can't think of a response to that. Would you like to add a response?")
                newAnswer: str = input("New Answer: ")

            if newAnswer.lower() != 'skip':
                brain["questions"].append({"question": userQuestion, "response": newAnswer})
                saveBrain('brain.json', brain)
                print('Brian: Thank you for teaching me!')

if __name__ == '__main__':
    Brian()