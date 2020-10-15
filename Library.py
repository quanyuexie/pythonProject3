# Author: Quanyue Xie
# Date: 10/14/2020
# Description：this is a library simulator which has three class
# LibraryItem, Patron, and Library. All data memebers should be private

import time
class LibraryItem:
    #initialized
    def __init__(self,title,location,checked_out_by=None,requested_by=None):
        self._library_item_id = None
        self._title = title
        self._location = location
        self._checked_out_by = checked_out_by
        self._requested_by = requested_by
        self._date_checked_out = None

    #def a check out length function so that it can be called in library class
    def get_check_out_length(self):
        return 0

    #when a LibraryItem is checked out, this will be set to the current_date of the Library
    def date_checked_out(self,current_date):
        self._date_checked_out = current_date

    #get and set
    def get_library_item_id(self):
        return self._library_item_id

    def set_library_item_id(self,library_item_id):
        self._library_item_id = library_item_id

    def get_title(self):
        return self._title

    def set_title(self,title):
        self._title = title

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def get_checked_out_by(self):
        return self._checked_out_by

    def set_checked_out_by(self,checked_out_by):
        self._checked_out_by = checked_out_by

    def get_requested_by(self):
        return self._requested_by

    def set_requested_by(self,requested_by):
        self._requested_by = requested_by

    def get_date_checked_out(self):
        return self._date_checked_out

    def set_date_checked_out(self,date_checked_out):
        self._date_checked_out = date_checked_out

# inherit from LibraryItem
class Book(LibraryItem):
    #according to eg., I add location and title
    def __init__(self,author,location,title):
        self._author = author
        self._location = location
        self._title = title

    def get_check_out_length(self):
        return 21

    #get author
    def get_author(self):
        return self._author

class Album(LibraryItem):
    def __init__(self,artist,location,title):
        self._artist = artist
        self._location = location
        self._title = title

    def get_check_out_length(self):
        return 14

    #get artist
    def get_artist(self):
        return self._artist

class Movie(LibraryItem):
    def __init__(self,director,location,title):
        self._director = director
        self._location = location
        self._title = title

    def get_check_out_length(self):
        return 7

    #get director
    def get_director(self):
        return self._director

class Patron:
    #initialized
    def __init__(self,patron_id,name):
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = {}
        self._fine_amount = None

    #returns the fine_amount
    def get_fine_amount(self):
        return self._fine_amount
    #get and set
    def get_checked_out_items(self):
        return self._checked_out_items

    def set_fine_amount(self, fine_amount):
         self._fine_amount = fine_amount

    def set_checked_out_items(self, checked_out_items):
         self._checked_out_items = checked_out_items

    #adds the specified LibraryItem to checked_out_items
    def add_library_item(self, libraryItem):
        self._checked_out_items[libraryItem._id] = libraryItem

    #removes the specified LibraryItem from checked_out_items
    def remove_library_item(self,libraryItem):
        del self._checked_out_items[libraryItem._id]

    #fine could be positive or negative num
    def amend_fine(self,amount):
        if amount > 0:
            self._fine_amount += amount
        else:
            self._fine_amount -= amount


class Library:
    #initialized
    def __init__(self,holdings,members,current_date):
        self._holdings = {}
        self._members = {}
        self._current_date = 0

    # takes a LibraryItem object as a parameter and adds it to the holdings
    def add_library_item(self,libraryItem):
        self._holdings[libraryItem.get_library_item_id()] = libraryItem

    #takes a Patron object as a parameter and adds it to the members
    def add_patron(self,patron):
        self._members[patron._patron_id] = patron

    def get_library_item_from_id(self,id):
        #None if no such LibraryItem is in the holdings
        if id not in self._holdings.keys():
            return None
        #returns the LibraryItem object corresponding to the ID parameter,
        else:
            return self._holdings[id]

    def get_patron_from_id(self,id):
        #None if no such Patron is a member
        if id not in self._members.keys():
            return None
        else:
            #returns the Patron object corresponding to the ID parameter
            return self._members[id]

    def check_out_library_item(self,patron_id,library_item_id):
        if patron_id not in self._members.keys():
            print("patron not found")
            return "patron not found"
        else:
            patron = self._members(patron_id)
        #if the specified LibraryItem is not in the Library's holdings
        if library_item_id not in self._holdings.keys():
            print("item not found")
            return "item not found"
        else:
            #get libraryItem from holdings
            libraryItem = self._holdings[library_item_id]
            if libraryItem.get_date_checked_out() is not None:
                print("item already checked out")
                return "item already checked out"
            else:
                #I am not sure if the date should be the local time
                libraryItem.set_date_checked_out(time.strftime('%Y-%m-%d',time.localtime(time.time())))
                libraryItem.set_checked_out_by(patron._patron_id)
                libraryItem.set_location("asd")
            if libraryItem.get_requested_by() is not None:
                print("item on hold by other patron")
                return "item on hold by other patron"
            else:
                #if the LibraryItem was on hold for this Patron
                libraryItem.set_requested_by(patron._patron_id)
                patron.set_checked_out_items(libraryItem)
                print("check out successful")
                return "check out successful"


    def return_library_item(self,library_item_id):
        if library_item_id not in self._holdings.keys():
            print("item not found")
            return "item not found"
        else:
            libraryItem = self._holdings[library_item_id]
            #if the LibraryItem is not checked out
            if libraryItem.get_date_checked_out() is None:
                print("item already in library")
                return "item already in library"
                patron.set_checked_out_items(libraryItem)
            else:
                print("return successful")
                return "return successful"

    def request_library_item(self,patron_id,library_item_id):
        #if the specified Patron is not in the Library's members
        if patron_id not in self._members.keys():
            print("patron not found")
            return "patron not found"
        else:
            patron = self._members(patron_id)
        #if the specified LibraryItem is not in the Library's holdings
        if library_item_id not in self._holdings.keys():
            print("item not found")
            return "item not found"
        else:
            libraryItem = self._holdings[library_item_id]
            #if the specified LibraryItem is already requested
            if libraryItem.get_requested_by() is not None:
                print("item already on hold")
                return "item already on hold"
            else:
                libraryItem.set_requested_by(libraryItem)
                print("request successful")
                return "request successful"

    def pay_fine(self,patron_id,amount):
        if patron_id not in self._members.keys():
            print("patron not found")
            return "patron not found"
        else:
            #update the Patron's fine
            patron = self.members[patron_id]
            patron.amend_fine(amount)
            print("payment successful")
            return "payment successful"

    def increment_current_date(self):
        self._current_date += 1
        for libraryItem_id in self._holdings.keys():
            libraryItem = self._holdings(libraryItem_id)
            #if more than the return date, add 10 cents
            if libraryItem.get_date_checked_out() > libraryItem.get_check_out_length():
                patron_id = libraryItem.get_checked_out_by()
                patron = self._members[patron_id]
                patron.amend_fine(10)
