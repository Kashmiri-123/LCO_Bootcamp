class FileManagement(object):
    
    def __init__(self):
        
        self.filename = "database.txt"
        try:
            self.f = open(self.filename, "a")
        except:
            print("Error in creating file...")
            
    def insert_data(self, data):
        try:
            with open(self.filename, 'a') as f:
                f.write(data[0]+"\n")
                f.write(data[1]+"\n")
                f.write(data[2])
                f.write("\n\n")
            return True
        except:
            return False
        
    def read_data(self):
        data = ""
        final_list = []
        try:
            with open(self.filename) as f:
                data = f.read()
                
            user_chunk = data.split("\n\n")
            
            for item in user_chunk[:-1]:
                
                single_chunk = item.split("\n")
                final_list.append((single_chunk[0],single_chunk[1],single_chunk[2]))
            return final_list
        except:
            return False
    
    def search_data(self,search_name):
        data = ""
        with open(self.filename) as f:
            data=f.read()
            final_list = []
            user_chunk = data.split("\n\n")
            for item in user_chunk[:-1]:
                single_chunk = item.split("\n")
                if search_name==single_chunk[0]:
                    print()
                    final_list.append((single_chunk[0],single_chunk[1],single_chunk[2]))
                    return final_list
        return False
    
    def update_data(self,search_name,new_name):
        data=""
        with open(self.filename) as f:
            data=f.read()
            final_list=[]
            user_chunk=data.split("\n\n")
            for item in user_chunk[:-1]:
                single_chunk = item.split("\n")
                if search_name==single_chunk[0]:
                    old_name=single_chunk[0]
                    if len(new_name)>0:
                        single_chunk[0]=new_name
                        with open(self.filename,"r") as f:
                            new_file=f.read()
                        new_file=new_file.replace(old_name,single_chunk[0])
                        with open(self.filename,'w') as f:
                                f.write(new_file)
                        print("Name is successfully changed")
                        return final_list
                    else:
                            return "Wrong Input"

    def delete_data(self,id):
        if not self.read_data():
            


def main():
    
    db = FileManagement()
    
    print("\n1. Insert Data")
    print("\n2. View Data")
    print("\n3. Search Data")
    print("\n4. Update Data")
    print("\n5. Delete Data")

    choice = input("\n\nEnter your choice : ")
    
    if choice == "1":
        
        name = input("\nEnter a name : ")
        email = input("Enter a email : ")
        passw = input("Enter a password : ")
        
        if db.insert_data([name, email, passw]):
            print("\nData Added!")
        else:
            print("Oops! Something went wrong!")
            
    elif choice == "2":
        
        print("\nUser Data\n")
        
        if db.read_data():
            for index, item in enumerate(db.read_data()):
                
                print("Sl No : " + str(index+1))
                print("Name : " + item[0])
                print("Email : " + item[1])
                print("Password : " + item[2])
                print()
    
    elif choice=="3":
        search_name=input("Enter name : ")
        if db.search_data(search_name):
            for index, item in enumerate(db.search_data(search_name)):
                print("Name : " + item[0])
                print("Email : " + item[1])
                print("Password : " + item[2])
                print()

    elif choice=="4":
        search_name=input("Enter name : ")
        new_name=input("Enter the new name  : ")
        if db.update_data(search_name,new_name):
            for index,item in enumerate(db.update_data(search_name,new_name)):
                print("Name : " + item[0])
                print("Email : " + item[1])
                print("Password : " + item[2])
                print()

    elif choice=="5":
        pass



main()