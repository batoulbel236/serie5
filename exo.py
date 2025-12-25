#Dictionary
books = {
    "978-0134685991":{
    "Titel": "Effective Python",
    "Author":"Brett Slatkin",
    "Year":"2019",
    "copie":"3",
    "Gener": "Programming",
    },
    
    "978-0135957059":{
     "Titel":"The Pragmatic Programmer",
     "Autohr":"David Thomas",
     "Year":"2019",
     "copie":"2",
     "Gener":"Programming" 
     },
      
    "978-0132350884":{
     "Titel":"Clean Code",
     "Author":"Robert Martin",
     "Years":"2008",
     "copie":"4",
     "Gener":"Programing"     
     },
 }

Libery_members ={
     "M001":{ 
    "Name":"Alice Johnson",
    "Email":"alice@university.edu",
    "Type":"student",
    "Join date":"(2024,9,1)",
   },

    "M002":{
    "Name":"Bob smith",
    "Email":"bob@university.edu",
    "Type":"Faculty",
    "Join date":"(2024,9,1)",
     },

    "M003":{
    "Name":"carol white",
    "Email":"carol@university.edu",
    "Type":"student",
    "join date":"(2024, 10, 15)"
     },

    }
#List
Borrowd_books = {
"M001" :["978-0134685991", "978-0135957059"],
"M002" :["978-0132350884"],
"M003" :["978-0134685991"], 
}
  
#Set
Book_gener = {"Programming, Fiction, Science, History, Mathematics, Art"}
#Dictionary
Library_hours ={
    "Monday": "9:00 AM - 8:00 PM",
    "Tuesday": "9:00 AM - 8:00 PM",
    "Wednesday": "9:00 AM - 8:00 PM",
    "Thursday": "9:00 AM - 8:00 PM",
    "Friday": "9:00 AM - 6:00 PM",
    "Saturday": "10:00 AM - 4:00 PM",
    "Sunday": "Closed"
}
#list
Popular_books =[
    ("978-0134685991","borrowed 45 times"),
    ("978-0132350884","borrowed 38 times"),
    ("978-0135957059","borrowed 32 times"),
  ]

#Set
Reserved_ISBNs ={
    "978-0134685991",
    "978-0135957059",
    "978-0132350884",
}

isbn ="978-0134685991"
print(books[isbn])

ID = "M001"
print(Libery_members[ID])

ID = "M001"
print(Borrowd_books[ID])

geners_add ="Political"
print(Book_gener[geners_add])

ISBN = "978-0135957059"
print("ISBN in reservedb_books")





