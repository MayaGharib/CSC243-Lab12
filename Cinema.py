class Hall:
    def __init__(self,name,seats):
        self.name=name
        self.__seats=seats
    def get_seats(self):
        return self.__seats
    def _has_seats(self):
        return self.__seats>0
    def has_seats(self):
        return self._has_seats()
    def set_seats(self,n):
        if type(n)==int and 0<=n<=100:
            self.__seats=n
        else:
            print("Invalid seats.")
    def __str__(self):
        return "Hall "+self.name+": "+str(self.__seats)+" seats"

class Guest:
    def __init__(self,name,tickets):
        self.name=name
        self.__tickets=tickets

    def get_tickets(self):
        return self.__tickets

    def add_tickets(self,n):
        if n>0:
            self.__tickets+=n
        else:
            print("Invalid amount.")

    def __str__(self):
        return self.name+": "+str(self.__tickets)+" tickets"

