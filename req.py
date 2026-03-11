import requests
url = "https://codeforces.com/api/user.status?handle=Souvik19"
url_fetch = "https://codeforces.com/api/user.info?handle"
name = input("Enter handle name:");
# payload = {'handles':name}
response  = requests.get(url)
data = response.json();
print(data)

# lst = data["result"]
# for content in lst:
#     print("Contribution :" ,content["contribution"])
#     print("Rating :",content["rating"])
#     print("Rank :",content["rank"])
#     print("Handle name :",content["handle"])
#     print("Max Rating :",content["maxRating"])