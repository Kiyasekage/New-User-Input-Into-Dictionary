def add_user(i_user_name,i_favorite_languange,i_experience):
    user = {}
    user["user_name"] = i_user_name
    user["favorite_languange"] = i_favorite_languange
    user["experience"] = i_experience
    programming_language.append(add_user)
    print(programming_languange)
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
u_n = input("Username : ")
f_l = input("Favorite_Languange(s) : ")
e = int(input("Years(only enter number) : "))
add_user(u_n,f_l,e)
