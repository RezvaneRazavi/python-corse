from prettytable import PrettyTable
from classMedia import Media

class Series(Media):
    def __init__(self, ID, name , director , IMDB_score , url , casts, seasons, episodes):
        super().__init__(ID,  name , director , IMDB_score , url , casts)

        
        self.seasons = seasons
        self.episodes = episodes

    def showInfo(self):
        my_table = PrettyTable()
        my_table.field_names = ["ID", "Name", "Director", "Score", "cast", "Seasons", "Episodes"]
        my_table.add_row([self.ID, self.name, self.director, self.score, self.casts, self.seasons, self.episodes])
        print(my_table)

    @staticmethod   
    def add(other):
        
        ID = input("Enter ID: ")  
        name = input("Enter Name: ")
        director = input("Enter name of director: ")
        score = input("Enter IMDB score: ")
        url = input("Enter URL: ")
        casts = input("Enter names of three stars with comma in betweens: ")
        seasons = input("Enter number of seasons: ")
        episodes = input("Enter number of episodes: ")

        new_obj = Series(ID, name, director, score, url, casts, seasons, episodes)
        other.append(new_obj)
        
    def edit(self):
        print("You have chosen", self.name, "to be edited")
        print("which data you wanna edit?")
        print("1- Name")
        print("2- Director")
        print("3- Score")
        print("4- URL")
        print("5- Casts")
        print("6- Number of Seasons")
        print("7- Number of Episodes")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_name = input("Enter the new Name: ")
            self.name = new_name
        elif choice == 2:
            new_director = input("Enter the new Director: ")
            self.director = new_director
        elif choice == 3:
            new_score = input("Enter the new Score: ")
            self.score = new_score
        elif choice == 4:
            new_url = input("Enter the new URL: ")
            self.url = new_url
        elif choice == 5:
            new_casts = input("Enter the new Casts: ")
            self.casts = new_casts
        elif choice == 6:
            new_seasons = input("Enter the new number of seasons: ")
            self.seasons = new_seasons
        elif choice == 7:
            new_episodes = input("Enter the new number of episodes: ")
            self.episodes = new_episodes

        print("Data is updated successfully!")