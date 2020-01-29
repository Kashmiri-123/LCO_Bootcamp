class File_handling:
    
    def __init__(self):
        self.filename = "File_gui.txt"
        
        try:
            self.f = open('File_gui.txt', 'a+')
        except:
            print("File can't be opened")
    
    def write(self, data):
        try:
            with open (self.filename, 'a') as f:
                f.write(data[0]+"\n")
                f.write(data[1]+"\n")
                f.write(data[2]+"\n\n")
            return True
        except:
            return False
    
    def read(self):
        
        data = ""
        final_list = []
        
        try:
            with open (self.filename, 'r') as f:
                data = f.read()
                chunck = data.split("\n\n")

            for item in chunck[:-1]:
                piece = item.split("\n")
                final_list.append((piece[0],piece[1],piece[2]))

            return final_list
        
        except:
            return False
    
    def search(self, id):
        all_data = ""
        
        with open (self.filename, 'r') as f:
            all_data = f.read()
            chunck = all_data.split("\n\n")
            
        if int(id) < 1 or int(id) >= len(chunck): return False

        for index, item in enumerate(chunck[:-1]):
            if index == int(id)-1:
                item = item.split("\n")
                print("SI No: " + str(index+1))
                print("Name: " + item[0])
                print("E-mail: " + item[1])
                print("Password: " + item[2])
                print()
        return True
    
    def update(self, id):
        all_data = ""
        
        with open (self.filename, 'r') as f:
            all_data = f.read()
            chunck = all_data.split("\n\n")
            
        if int(id) < 1 or int(id) >= len(chunck): return False

        f = open(self.filename, 'w')
        f.close()
            
        for index, item in enumerate(chunck[:-1]):

            if index != int(id)-1:
                item = item.split("\n")
                with open (self.filename, 'a') as f:
                    f.write(item[0]+"\n")
                    f.write(item[1]+"\n")
                    f.write(item[2]+"\n\n")
                    
            elif index == int(id)-1:
                item = item.split("\n")
                
                print("1)Edit name"," 2)Edit Email", " 3)Edit Password")
                choice = input()
                
                if choice == '1': item[0] = input("\nEnter name: ")
                elif choice == '2': item[1] = input("\nEnter email: ")
                elif choice == '3': item[2] = input("\nEnter password: ")
                
                with open (self.filename, 'a') as f:
                    f.write(item[0]+"\n")
                    f.write(item[1]+"\n")
                    f.write(item[2]+"\n\n")

        return True
    
    def delete(self, id):
        
        all_data = ""
        try:
            with open (self.filename, 'r') as f:
                all_data = f.read()
                chunck = all_data.split("\n\n")
                
            if int(id) < 1 or int(id) >= len(chunck): return False
            
            f = open(self.filename, 'w')
            f.close()
            
            for index, item in enumerate(chunck[:-1]):
                
                if index != int(id)-1:
                    
                    item = item.split("\n")
                    with open (self.filename, 'a') as f:
                        f.write(item[0]+"\n")
                        f.write(item[1]+"\n")
                        f.write(item[2]+"\n\n")

            return True
        
        except:
            return False

def main():
    
    F_obj = File_handling()
    
    while 1:
        print("1)Insert Data", "2)View Data", "3)Delete Data", "4)Search Data" , "5)Update Data","6)Exit\n\n")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("\nEnter name: ")
            mail = input("Enter email: ")
            password = input("Enter password: ")

            if F_obj.write([name,mail,password]): print("\nData Successfully Added\n")
            else: print("\nError in Data Insertion\n")

        elif choice == '2':
            if F_obj.read():
                print("\nAll User Data\n")
                for index, item in enumerate(F_obj.read()):
                    print("SI No: " + str(index+1))
                    print("Name: " + item[0])
                    print("E-mail: " + item[1])
                    print("Password: " + item[2])
                    print()

            else: print("\nError in Reading Data\n")

        elif choice == '3':
            id = input("Enter the ID of the record to delete: ")
            if F_obj.delete(id): print("\nRemoved the record successfully\n")
            else: print("\nDelete Unsuccessful\n")
                
        elif choice == '4':
            id = input("Enter the ID of the record to Search: ")
            if F_obj.search(id): print("Required Record Exists and is Displayed\n")
            else: print("Record doesn't exist\n")
                
        elif choice == '5':
            id = input("Enter the ID of the record to Update: ")
            if F_obj.update(id): print("Record Updated")
            else: print("Record doesn't exist\n")
                
        elif choice == '6': break

        else: print("Choose a valid input")

main()