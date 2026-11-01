import json
def add_user(i_user_name,i_favorite_languange,i_experience):
    user = {}
    user["user_name"] = i_user_name
    user["favorite_languanges"] = i_favorite_languange
    user["experience"] = i_experience
    programming_language.append(user)
    print("\nUpdated Version : \n", json.dumps(programming_language,indent = 4))
programming_language = [
    {"user_name" : "Elshad",
     "favorite_languages" : ["Python", "Java", "C#"],
     "experience": 10 
    },
    {"user_name":"Renad",
     "favorite_languages" : ["Scratch","Python"],
     "experience" : 2
    },
]

print("Welcome to the Programmer Login Page\nPlease fill your identity below")
status = input("What's your current position?[A : Admin, C : Client]").upper().strip()
if status == "A":
    password_admin = "admin123456"
    password = input("Password : ")
    if password != password_admin:
        print("Password Incorrect!")
if status == "C":
    ans = "YES"
    while ans == "YES":
        print("Please fill your identity below")
        u_n = input("Username : ")
        f_l = input("Favorite_Languange(s) : ").capitalize().split(",")
        e = int(input("Years(only enter number) : "))
        add_user(u_n,f_l,e)
        ans = input("Do you want to continue a new user?[Yes/No]").upper().strip()
