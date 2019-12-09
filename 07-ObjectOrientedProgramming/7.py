class Student():
    university='UEK Kraków'
    major='Informatyka Stosowana'
    nr=100000
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname
        self.album=Student.nr
        Student.nr += 1
    def __str__(self):
        return f'''
                    Name: {self.name}
                    Last name: {self.lastname}
                    Album No.: {self.album}
                    Major: {Student.major}
                    University: {Student.university}'''
s1=Student('Wacław', 'POTOCKI')
s2=Student('Adam', 'NOWAK')
s3=Student('1', '2')
print(s1)
print(s2)
print(s3)