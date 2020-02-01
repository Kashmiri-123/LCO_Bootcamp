class Backend():
    def __init__(self):
        try:
            self.f=open("data.txt","a+")
        except:
            print("Something went wrong with the file.")
    

    def register(self,data):
        try:
            with open("data.txt", 'a+') as f:
                f.write("Name : "+ data[0]+"\n")
                f.write("Email : " + data[1]+"\n")
                f.write("Password : " + data[2]+"\n\n\n")
            return True
        except:
            return False

    
    def view_data(self):
        final_user_list=[]
        try:
            with open("data.txt","r") as f:
                data=f.read()
                new_list=data.split("\n\n\n")
                for items in new_list[:-1]:
                    single_users = items.split('\n')
                    final_user_list.append([
                        single_users[0],
                        single_users[1],
                        single_users[2]
                    ])
            return final_user_list
        except:
            return False

    def edit_data(self):
        try:
            capture=self.view_data()
            mail=input("Enter admin mail : ")
            passwd=input("Enter admin pass : ")
            if mail=="xyz@gmail.com" and passwd=="123":
                answer=input("What do you want to change name/mail/password?")
                if answer=="name":
                    name=input("Enter name : ")
                    new_name=input("Enter new name : ")
                    name="Name : "+name
                    for index,value in enumerate(capture):
                        if value[0]==name:
                            value[0]="Name : "+new_name
                            print(value[0])
                            with open("data.txt","r") as f:
                                new_file=f.read()
                            new_file=new_file.replace(name,value[0])
                            with open("data.txt","w") as f:
                                f.write(new_file)
                            print("Data changed successfully")


                elif answer=="mail":
                    email=input("Enter email : ")
                    new_mail=input("Enter new email : ")
                    email="Email : "+email
                    for index,value in enumerate(capture):
                        if value[1]==email:
                            value[1]="Email : "+new_mail
                            with open("data.txt","r") as f:
                                new_file=f.read()
                            new_file=new_file.replace(email,value[1])
                            with open("data.txt","w") as f:
                                f.write(new_file)
                            print("Data changed successfully")

                else:
                    print("Wrong input")
            else:
                print("Not an admin")

            return new_file

        except:
            return False


    def delete_data(self):
        try:

            user_id=int(input("Enter id to be deleted : "))

            with open("data.txt","r") as f:
                data=f.read()
                new_list=data.split("\n\n\n")

            if user_id<1 or user_id>=len(new_list):
                return False

            f = open("data.txt","w")
            f.close()

            for index,item in enumerate(new_list[:-1]):
                if index != user_id-1:
                    item=item.split("\n")

                    with open("data.txt",'a') as f :
                        f.write(item[0]+"\n")
                        f.write(item[1]+"\n")
                        f.write(item[2]+"\n\n")
                    
            return True


        except:

            return False




def main():

    object=Backend()

    print("1.Register ")
    print("2.View data ")
    print("3.Edit data ")
    print("4.Delete data ")

    choice=int(input("Enter your choice: "))

    print("\n\n")

    if choice==1:
        name=input("Enter your name : ")
        email=input("Enter your mail : ")
        password=input("Enter your password : ")

        if object.register([name,email,password]):
            print("Registration Successful!")
        else:
            print("Registration failed!")
    
    elif choice==2:
        if object.view_data():
            for values in object.view_data():
                print(values[0])
                print(values[1])
                print(values[2],"\n\n")


        else:
            print("Data cannot be displayed!")

    elif choice==3:
        if object.edit_data():
            print("Done")

        else:
            print("Not an authenticated user.")

    elif choice==4:
        if object.delete_data():
            print("Data deleted")
        else:
            print("Error in deleting data.")


        





main()
