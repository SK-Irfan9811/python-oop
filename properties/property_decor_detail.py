#Traditional way of using property decorater
class Movie:

    def __init__(self,name, rating):
        self.set_rating(rating)
        self.set_name(name)

    def get_rating(self):
        return self._rating
    
    def set_rating(self, rating):
        if rating in ["G", "PG", "PG-13", "R", "NC-17"]:
            self._rating = rating
        else:
            raise ValueError("Invalid rating")
        
    def del_rating(self):
        del self._rating    

    def get_name(self):
        print("getting movie name...")
        return self._name   
    
    def set_name(self, name):
        print("setting movie name...")
        self._name = name

    rating=property(fget=get_rating, fset=set_rating, fdel=del_rating)
    name=property(fget=get_name, fset=set_name)

spider_man=Movie("Spider Man", "G")
print(spider_man.__dict__)
Movie.name.setter("Spider Man 2")
print(spider_man.__dict__)