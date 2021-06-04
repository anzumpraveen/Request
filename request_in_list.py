import requests
import json

api1="http://saral.navgurukul.org/api/courses"
a=requests.get(api1)
print(a)
b=a.json()
with open("saral_course.json","w")as f:
    json.dump(b,f,indent=4)
    data=(b["availableCourses"])
count=1
for i in range(0,len(data)):
    course_name=data[i]["name"]
    course_id=data[i]["id"]
    print(count,course_name,course_id)

    count+=1
# second_round_______
user = int(input("enter id number="))
user_id = b["availableCourses"][user-1]["id"]
api2="https://saral.navgurukul.org/api/courses/"+str(user_id)+"/exercises"
x=requests.get(api2)
y=x.json()
with open("exercise.json","w")as fp:
    json.dump(y,fp,indent=4)
my_data=y["data"]
i=1
while i<len(my_data):
    print(i+1,my_data[i]["name"])
    child = my_data[i]["childExercises"]
    slug = my_data[i]["slug"]
    if child ==[]:
        print("   ",slug)
    else:
        j=1
        while j<len(child):
            print("  ",j+1,child[j]["name"])
            j+=1
    i+=1
user1=int(input("enter parent:-"))
user1 = user1
print(my_data[user1]["name"])
slug = my_data[user1]["slug"]
if my_data[user1]["childExercises"]==[]:
    print(slug)
    slug_api = requests.get("https://saral.navgurukul.org/api/courses/"+str(user)+"/exercise/getBySlug?slug="+my_data[user1]["slug"])
    slug_data = slug_api.json()
    with open("slug_id.json","w") as f:
        json.dump(slug_data,f,indent=4)
    slug_input = input("Do you want slug:yes or no").lower()
    if slug_input=="yes":
        print(slug_data["content"])
else:
    i=1
    while i<len(my_data[user1]["childExercises"]):
        print(i+1,my_data[user1]["childExercises"][i]["name"])
        i+=1
    child_input = int(input("Enter the question number"))
    child_api = requests.get("https://saral.navgurukul.org/api/courses/"+str(user)+"/exercise/getBySlug?slug="+my_data[user1]["childExercises"][child_input-1]["slug"])
    child_data = child_api.json()
    with open("child_id.json","w") as f:
        json.dump(child_data,f,indent=4)
    print(child_data)