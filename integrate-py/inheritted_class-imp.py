class classroom:                   #mentioned first class
    
    attendees = "student"

    def classinsight(self):           #mentioned an function within the first class
        print("This class is disciplined")

class school(classroom):           #mentioned second class, but all the items from irst class are also inheritted 
    
    lecturer = "teachers"

    def schoolinsight(self):          #mentioned an function for the second class
        print("This school is good")

c = classroom()                      #onboarding variable c into first class

s = school()                         #onboarding variable s into second class

c.classinsight()                     #calling variable c with its own function, ofcourse 'self' is mentioned, no print command required

s.schoolinsight()                    #calling variable s with its own function, similar to above

s.classinsight()                     #now calling variable s with the first function, basically cross clsss-functions, it will return value                                     from first function, because inherittence has already happened above within both the classes.

