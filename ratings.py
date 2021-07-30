"""Restaurant rating lister."""



def rest_rating(filename):
    fileopened=open(filename)
    scores = {}
    
    for line in fileopened:
        line=line.strip()
        resturant, rating=line.split(":")
        scores[resturant]=int(rating)
    
        
        for restruant, rating in sorted(scores.items()):
            print(f"The rating of {resturant} is a {rating}")
            

