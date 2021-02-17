import sys
from datetime import datetime,timedelta
#######################################################################
Hourly=12
Daily=15
Weekly=25
Storeddata={}
#######################################################################
class BookRental:

    def __init__(self,listofbooks):#this init method is the first method to be invoked when you create an object
            #what attributes does a library in general have? - for now, let's abstract and just say it has availablebooks (we're not going to program the shelves, and walls in!)
        self.availablebooks=listofbooks

    def displayAvailablebooks(self):
        print("The books we have in our library are as follows:")
        print("================================")
        for book in self.availablebooks:
            print(book)
    def lendBook(self,requestedBook):
        if requestedBook in self.availablebooks:
            print("The book you requested has now been borrowed")
                
            print("""Enter the Package of book you want:
                1.Hourly($12)
                2.Daily($15)
                3.Weekly($25)
                4.Family Package""")
            selectpackage=input("Enter choice:")
            if(selectpackage=='1'):
                Storeddata["book"]=requestedBook
                Storeddata["price"]=12
                Storeddata["package"]="Hourly"
                time=datetime.now()
                Storeddata["time"]=time
                print("Please pay $",Hourly,"at the counter(Hourly Package) at time:",time)
                self.availablebooks.remove(requestedBook)
            elif(selectpackage=='2'):
                Storeddata["book"]=requestedBook
                Storeddata["price"]=15
                Storeddata["package"]="Dialy"
                time=datetime.now()
                Storeddata["time"]=time
                print("Please pay $",Daily,"at the counter(Daily Package)at time:",time)
                self.availablebooks.remove(requestedBook)
            elif(selectpackage=='3'):
                Storeddata["book"]=requestedBook
                Storeddata["price"]=25
                Storeddata["package"]="Weekly"
                time=datetime.now()
                Storeddata["time"]=time
                print("Please pay $",Weekly,"at the counter(Weekly Package)at time:",time)
                self.availablebooks.remove(requestedBook)
            elif(selectpackage=='4'):
                Storeddata["book"]=requestedBook
                per=int((Weekly*30)/100)
                price=25-per
                Storeddata["price"]=price
                Storeddata["package"]="Family"
                time=datetime.now()
                Storeddata["time"]=time
                print("Please pay $",price,"at the counter(Weekly and Family Package)at time:",time)
                self.availablebooks.remove(requestedBook)
            else:
                print("Sorry We Dont Have any more packages")

        else:
            print("Sorry the book you have requested is currently not in the library")


    def addBook(self,returnedBook):
        self.availablebooks.append(returnedBook)
        print("Thanks for returning your borrowed book")
            
############################################################################################
class Student:
      def requestBook(self):
            print("Enter the name of the book you'd like to borrow>>")
            self.book=input()
            return self.book

      def returnBook(self):
            print("Enter the name of the book you'd like to return>>")
            self.book=input()
            time2=datetime.now()
            c1=Storeddata["time"]-time2
            c=int(c1.total_seconds()/60)
            if(self.book==Storeddata["book"]):
                if(Storeddata["package"]=="Hourly"):
                    if(c<=1):
                        print("Hello Customer,Your bill of book is",Storeddata["price"],"and",Storeddata["package"],"package and Issused at",Storeddata["time"],"and Returned at",time2)
                        return self.book
                    else:
                        print("You need to pay the Fine fee of $20.So,Total Bill is:",Storeddata["price"]+20)
                        print("Hello Customer,Your bill of book is",Storeddata["price"]+20,"and",Storeddata["package"],"package and Issused at",Storeddata["time"],"and Returned at",time2)
                elif(Storeddata["package"]=="Dialy"):
                    if(c<=24):
                        print("Hello Customer,Your bill of book is",Storeddata["price"],"and",Storeddata["package"],"package and Issused at",Storeddata["time"],"and Returned at",time2)
                        return self.book
                    else:
                        print("You need to pay the Fine fee of $20.So,Total Bill is:",Storeddata["price"]+20)
                        print("Hello Customer,Your bill of book is",Storeddata["price"]+30,"and",Storeddata["package"],"package and Issused at",Storeddata["time"],"and Returned at",time2)
                elif(Storeddata["package"]=="Weekly"):
                    if(c<=144):
                        print("Hello Customer,Your bill of book is",Storeddata["price"],"and",Storeddata["package"],"package and Issused at",Storeddata["time"],"and Returned at",time2)
                        return self.book
                    else:
                        print("You need to pay the Fine fee of $20.So,Total Bill is:",Storeddata["price"]+20)
                        print("Hello Customer,Your bill of book is",Storeddata["price"]+40,"and",Storeddata["package"],"package and Issused at",Storeddata["time"],"and Returned at",time2)
                elif(Storeddata["package"]=="Family"):
                    if(c<=144):
                        print("Hello Customer,Your bill of book is",Storeddata["price"],"and",Storeddata["package"],"package and Issused at",Storeddata["time"],"and Returned at",time2)
                        return self.book
                    else:
                        print("You need to pay the Fine fee of $20.So,Total Bill is:",Storeddata["price"]+20)
                        print("Hello Customer,Your bill of book is",Storeddata["price"]+35,"and",Storeddata["package"],"package and Issused at",Storeddata["time"],"and Returned at",time2)
##################################################################################################################################################################################################################
def main():            
      library=BookRental(["The Last Battle","The Screwtape letters","The Great Divorce"])
      student=Student()
      done=False
      while done==False:
            print(""" ======BOOK RENTED MENU=======
                  1. Display all available books
                  2. Request a book
                  3. Return a book
                  4. Exit
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                        library.displayAvailablebooks()
            elif choice==2:
                        library.lendBook(student.requestBook())
            elif choice==3:
                        library.addBook(student.returnBook())
            elif choice==4:
                  sys.exit()
                  
main()
