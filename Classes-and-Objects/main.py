class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name=name
        self.age=age
        self.tracks=tracks
        self.score=score
    
        print("The name  ", name, " and my age is ", age, "I belong to ", tracks, "my present grade is ", score)

    def change_name(self, name):
        self.name = name
        print("The name  ", name, )
    def change_age(self, age):
        self.age = age
        print("And my age is ", age,)
    def add_track(self, track):
        self.track = track
        print("I belong to ", track)
    def get_score(self, score):
        self.score = score
        print("My present grade is", score)
        return self.score
        
        
        
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(100)
