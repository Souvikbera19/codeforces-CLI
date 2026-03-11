import requests

USER_HANDLE = input()
url_user_status = f"https://codeforces.com/api/user.status?handle={USER_HANDLE}"
problemRating = int(input("Enter problem rating"))
url_problemset = "https://codeforces.com/api/problemset.problems"
response_user_status= requests.get(url_user_status)
user_data = requests.get(url_user_status).json()

data = user_data["result"]
for p in data:
    if(p['verdict']=="OK"):
        problem = p['problem']
        if 'rating' in problem :
            print(problem['rating'],problem['contestId'],problem['name'])
# response_problemset = requests.get(url_problemset)
# data_problemset = response_problemset.json()
# problems = data_problemset['result']['problems']
# count = 0;
# for p in problems:
#     if 'rating' in p and p['rating']== problemRating:
#         print(p['contestId'],p['name'],p['tags'])
#         count+=1
#     if(count==100):
#         break
# print(data_problemset)
