import requests
import webbrowser
# from req import response
def solved_problems(handle):
    url = f"https://codeforces.com/api/user.status?handle={handle}"
    data = requests.get(url).json()
    solved = set()
    for content in data["result"]:
        if content["verdict"]=="OK":
            problem_data = content["problem"]
            solved.add((problem_data["contestId"],problem_data["index"]))
    return solved

def mashup_Problem(user1,user2,rating):
    solved_question1 = solved_problems(user1)
    solved_question2 = solved_problems(user2)
    solved_union = solved_question1|solved_question2
    problemSetURL = "https://codeforces.com/api/problemset.problems"
    data = requests.get(problemSetURL).json()
    for content in data["result"]["problems"]:
        if "rating" in content and content["rating"]==rating:
            key = (content["contestId"],content["index"])
            if key not in solved_union:
                return f"https://codeforces.com/problemset/problem/{content['contestId']}/{content['index']}"
    return None


link = mashup_Problem("Souvik19","ricecok",1100)
print("Problem:", link)
if link:
    webbrowser.open(link)