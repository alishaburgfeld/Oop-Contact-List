# from functools import cmp_to_key



class ContactList():
    # def __sort_by_name(a,b):  #this sorts the dictionaries based on their ages low to high
    #  if a["name"]-b["name"] >1:
    #     return 1
    #  elif a["name"]-b["name"]< 1:
    #    return -1
    #  else:
    #      return 0

    #initially I was trying to sort my list based on a private function, but I didn't know how I would pass my private function into my sort method on line 17
    def __init__(self,list_name,list):
        list_name=list_name
        self.list=sorted(list,key=lambda x: x['name'])

    def add_contact(self,name,number):
        contact={}
        contact["name"]=name
        contact["number"]=number
        self.list.append(contact)
        self.list=sorted(self.list,key=lambda x: x['name'])

    def remove_contact(self,name):
        for contact in self.list:
            if contact["name"]==name:
                self.list.remove(contact)

    def find_shared_contacts(self,ContactList):
        # matched=filter(lambda contact: contact["name"]==self.list["name"] and contact["number"]== self.list["number"],ContactList.list)
        # return matched
        # why isn't my filter working? when I return or print it it just says filtered object
        matched_two=[]
        for contact in self.list:
            if contact in ContactList.list:
                matched_two.append(contact)
        return matched_two


friends = ContactList("My Friends", [{"name":"Natalie", "number": "555-777-1144"}])
friends.add_contact("Kaylee","555-222-1414")
friends.add_contact("Mary","555-123-4567")
coworkers= ContactList("Coworkers", [])
coworkers.add_contact("Kaylee","555-222-1414")
coworkers.add_contact("Skyler","123-456-1232")
print(friends.find_shared_contacts(coworkers))
# print(matched)
print(friends.list)
# friends.remove_contact("Kaylee")
# print(friends.list)






