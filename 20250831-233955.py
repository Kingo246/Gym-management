import time
import os
members=[]
def clear_terminal():
    os.system("cls") if os.name=="nt" else os.system("clear")
print("\n\nwelcome to Gym membership management\n\n")
class Gym:
    def __init__(self,first_name,last_name,membership_id,status):
        self.first_name=first_name
        self.last_name=last_name 
        self.membership_id=membership_id
        self.status=status
    def display_members(self):
        print(f"first Name:{self.first_name}")
        print(f"last Name:{self.last_name}")
        print(f"membership_id:{self.membership_id}")
        print(f"membership_status:{self.status}")
        print("_"*20)
        time.sleep(1)
def search_members():
    print("\n\nsearch by:\n")
    print("1. membership id")
    print("2. first_name")
    print("3. membership status\n")
    your_choice=input("enter your choice:")
    if your_choice=="1":
        id_to_search=input("enter the membership id:")
        member_id=[i for i in members if i.membership_id==id_to_search]
        if member_id:
            for u in member_id:
                u.display_members()
        else:
            print(f"there's no member with this id {id_to_search}")
    elif your_choice=="2":
        first_name_to_search=input("enter the first name to search:").lower()
        member_first_name=[n for n in members if n.first_name.lower()==first_name_to_search]
        if member_first_name:
           for a in member_first_name:
               a.display_members()
        else:
            print(f"there's no member with this first name {first_name_to_search}")
    elif your_choice=="3":
        status_member=input("enter the membership status to search (active/inactive):").lower()    
        membership_status=[z for z in members if z.status==status_member]
        if membership_status:
            for k in membership_status:
                k.display_members()
        else:
            print("please enter status of your members!")
    else:
        print("please choose between 1 and 3")
def add_member():
    first_name=input("enter the first name:")
    last_name=input("enter the last name:")
    membership_id=input("enter the membership id:")
    status=input("enter membership status,or click enter:").lower()
    if status!="active":
        status="inactive" 
    else:
        status="active"
    return Gym(first_name,last_name,membership_id,status)
while True:
    print("choose an action:\n")
    print("1. add new member")
    print("2. display all members")
    print("3. search for a member")
    print("4. exit\n")
    the_choice=input("enter your choice:")
    if the_choice=="1":
        clear_terminal()
        members.append(add_member())
        print("member added successfully!")
    elif the_choice=="2":
        clear_terminal()
        if members:
            print("display all members....")
            time.sleep(1)
            for m in members:
                m.display_members()
        else:
            print("no member found!")
    elif the_choice=="3":
        clear_terminal()
        search_members()
    elif the_choice=="4":
        print("exiting....")
        time.sleep(1)
        break
    else:
        print("invalid choice please choose between 1 and 4")                     
                
       
           
                                   
            
                                  
                    
            
        
        
            
            
        
           