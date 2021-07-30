"""Restaurant rating lister."""



def rest_rating(filename):
    fileopened=open(filename)
    scores = {}
    
    for line in fileopened:
        line=line.strip()
        resturant, rating=line.split(":")
        score[resturant]=int(rating)
    
        
        for restruant, value in sorted(scores.items()):
            print(f"The rating of {resturant} is a {value}")
            

