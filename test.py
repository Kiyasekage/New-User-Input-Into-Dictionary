def add_user(i_user_name,i_favorite_languange,i_experience):
    user = {}
    user["user_name"] = i_user_name
    user["favorite_languanges"] = i_favorite_languange
    user["experience"] = i_experience
    programming_language.append(user)
    print(programming_language)
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
status = input("What's your current position?[A : Admin, C : Client]")
if status = "A":
    password_admin = "admin123456"
    password = input("Password : ")
    if password != password_admin:
        print("Password Incorrect!")
u_n = input("Username : ")
f_l = input("Favorite_Languange(s) : ")
e = int(input("Years(only enter number) : "))
add_user(u_n,f_l,e)
