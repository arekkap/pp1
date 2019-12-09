class Music():
    def __init__(self,author, title,album,year):
        self.author=author
        self.title=title
        self.album=album
        self.year=year
    def __str__(self):
        return f'''
                    Author: {self.author}
                    Title: {self.title}
                    Album: {self.album}
                    Year: {self.year}'''
a1=Music('Hollywood Undead', 'Bullet', 'American Tragedy', 'No idea')
a2=Music('Hollywood Undead', 'Comming in Hot', 'American Tragedy', 'No idea')
a3=Music('Hollywood Undead', 'Up in smoke', '???', 'No idea')
print(a1,a2,a3)