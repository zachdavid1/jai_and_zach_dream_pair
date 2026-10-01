from datetime import date

class Tracker():
    def __init__(self, today):
        self.friends = []
        self.today = today
    def add_friend(self, friend):
        self.friends.append(friend)

    def edit_name(self, old_name, new_name):
        for friend in self.friends:
            if friend.name == old_name:
                friend.name = new_name

    def edit_bday(self, old_bday, new_bday):
        for friend in self.friends:
            if friend.bday == old_bday:
                friend.bday = new_bday
    
    def upcoming_bdays(self):
        upcoming = {}
        today = self.today

        for friend in self.friends:
            friend_age = today[2] - friend.bday[2] 
            if (today[1] - friend.bday[1] < 0 and today[1] - friend.bday[1] > -3):
                upcoming[friend.name] = friend_age
            elif (friend.bday[1]-(today[1] - 12) < 3):
                upcoming[friend.name] = friend_age + 1
            elif today[1] - friend.bday[1] == 0:
                if friend.bday[0] >= today[0]:
                    upcoming[friend.name] = friend_age
            
        return upcoming


class Person():
    def __init__(self, name, bday):
        self.name = name
        self.bday = bday

