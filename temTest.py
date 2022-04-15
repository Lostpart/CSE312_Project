from user_CRUD import database_user as db_user
from manager import user_manager as um
if __name__ == "__main__":
    username1 = "howie"
    email1 = "howie@gmail.com"
    password1 = "haohuili"

    username2 = "shouyue"
    email2 = "shoouyue@email.com"
    password2 = "shiluo"

    username3 = "ywang298"
    email3 = "ywang298@email.com"
    password3 = "asbdkasb"

    username4 = "howie"
    email4 = "howie@gmail.com"
    password4 = "HaohuiLin"

    username5 = "test"
    email5 = "how ie@gmail.com"
    password5 = "HaohuiLin"

    user = []
    user.append((username1, email1, password1))
    user.append((username2, email2, password2))
    user.append((username3, email3, password3))
    user.append((username4, email4, password4))
    user.append((username5, email5, password5))
    for i in range(5):
        print(um.register(user[i][0], user[i][1], user[i][2]))

    # for i in range(5):
    #     # print(user[i][1])
    #     print(um.login(user[i][1], user[i][2]))