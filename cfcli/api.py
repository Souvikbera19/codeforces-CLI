import requests

BASE_URl = "https://codeforces.com/api"

def get_user_info(handle:str):
    user_url = f"{BASE_URl}/user.info?handles={handle}"
    data = requests.get(user_url).json()
    return data['result'][0]

def get_user_contest(handle:str):
    contest_url=f"{BASE_URl}/user.rating?handle={handle}"
    data = requests.get(contest_url).json()
    return data['result']

    
def solved_problem(handle:str):
    user_url = f"{BASE_URl}/user.status?handle={handle}"
    data = requests.get(user_url).json()
    solved_questions = set()
    for prob in data["result"]:
        if prob["verdict"]=="OK":
            problem_data = prob["problem"]
            solved_questions.add((problem_data["contestId"],problem_data["index"]))
    return solved_questions

def mashup_ques(handle1:str,handle2:str,rating:int):
    solved_1 = solved_problem(handle1)
    solved_2 = solved_problem(handle2)
    common_solve = solved_1|solved_2
    problemsetURL = f"{BASE_URl}/problemset.problems"
    data = requests.get(problemsetURL).json()
    for problem in data["result"]["problems"]:
        if "rating" in problem and problem["rating"]==rating:
            key = (problem["contestId"],problem["index"])
            if key not in common_solve:
                return f"https://codeforces.com/problemset/problem/{problem['contestId']}/{problem['index']}"
    return None