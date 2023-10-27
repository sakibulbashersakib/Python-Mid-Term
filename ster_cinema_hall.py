class Star_Cinema:
    __hall_list=[]
    def entry_hall(self,hall):
        Star_Cinema.__hall_list.append(hall)
class Hall(Star_Cinema):
    def __init__(self,row,cols,hall_no) -> None:
        self.seats={}
        self.show_list=[]
        self.row=row
        self.cols=cols
        self.hall_no=hall_no
        self.entry_hall(self)
    def entry_show(self,id,movie_name,time):
        movie=(id,movie_name,time)
        self.show_list.append(movie)
        self.seats[id]=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    def book_seats(self,id,s_lst):
        if id not in self.seats:
            print("\nSorry your show id is wrong. Please enter correct show id.\n")
            return
        for r,c in s_lst:
            if self.seats[id][r][c]==1:
                print("This seat is already booked. Please try another.")
                return
        for r,c in s_lst:
            if self.seats[id][r][c]==0:
                self.seats[id][r][c]=1
        print("\nSeat",*s_lst ,"is booked for",id,"\n")

    def view_show_list(self):
        print("--------------------")
        for item in self.show_list:
            print(f"MOVIE NAME: {item[1]}({item[0]}) SHOW ID: {item[0]} TIME: {item[2]}\n")
        print("--------------------")
    def view_available_seats(self,id):
        print(f"Available seat for {id}:")
        for i in self.seats:
            if i==id:
                for r in self.seats[i]:
                    for c in r:
                        print(c, end=" ")
                    print()

hall = Hall(4,4,9)
hall.entry_show("111", "Jawan Maji", "25/10/2023 11:00 AM")
hall.entry_show("333", "Sujon Moji", "25/10/2023 2:00 PM")
user=None
while(True):
    print("........WELCOME........")
    if user==None:
        print("1. VIEW ALL SHOW TODAY.")
        print("2. VIEW AVAILABLE SEATS.")
        print("3. BOOK TICKET.")
        print("4. EXIT.")
        ch=int(input("ENTER OPTION: "))
        print("\n")
        if ch==1:
            hall.view_show_list()
        elif ch==2:
            id=input("ENTER SHOW ID: ")
            if id!="111" and id!="333":
                print("\nSorry your show id is wrong. Please enter correct show id.\n")
            hall.view_available_seats(id)
        elif ch==3:
            id=input("ENTER SHOW ID: ")
            num=int(input("Number Of Ticket?: "))
            for i in range(num):
                row=int(input("ENTER SEAT ROW (0-3): "))
                col=int(input("ENTER SEAT COL (0-3): "))
                if row>=4 or col>=4:
                    print("\nYour seat is invalid.\n")
                    break
                lst=[(row,col)]
                hall.book_seats(id,lst)
        elif ch==4:
            user=None
            print("\n........Thank You.......\n")
        else:
            print("Please select right option.")