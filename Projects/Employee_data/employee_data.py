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
        try:
            with open("data.txt","r") as f:
                data=f.read()
            new_list=data.split("\n\n\n")
            return new_list
        except:
            return False

    def edit_data(self,user_input,old_value,new_value):
        try:
            # if user_input==1:
            #     with open("data.txt","r+") as f:
            #         data=f.read()
            #     new_list=data.split("\n\n\n")
            #     for item in new_list[:-1]:
            #         single_data=item.split("\n")
            #         print("ppp",single_data[0])
            #         if "Name : "+old_value==single_data[0]:
            #             single_data[0]=new_value
            #             with open("data.txt","r") as f:
            #                 new_file=f.read()
            #             new_file=new_file.replace(old_value,single_data[0])
            #             with open("data.txt","w") as f:
            #                 f.write(new_file)
            #                 break
            # return new_file


        except:
            return False



def main():
    object=Backend()
    print("1.Register ")
    print("2.View data ")
    print("3.Edit data ")

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
            for index,value in enumerate(object.view_data()[:-1]):
                print("Record "+str(index+1))
                print(value)
                print("\n")
        else:
            print("Data cannot be displayed!")

    elif choice==3:
        print("What do you want to change?")
        print("1.Name ")
        print("2.Email ")
        print("3.Password ")

        user_input=int(input("Enter your choice : "))

        if user_input==1:
            old_name=input("Enter the old name : ")
            new_name=input("Enter the new name : ")
            if object.edit_data(user_input,old_name,new_name):
                for index,value in enumerate(object.edit_data(user_input,old_name,new_name)):
                    # print("Record "+str(index+1))
                    print(value)
                    print("\n")
            else:
                print("Data could not be editted")
        
        if user_input==2:
            pass

        if user_input==3:
            pass





main()
