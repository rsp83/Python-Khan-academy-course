

def get_cherry_score(num_cherries):

    if num_cherries > 1 :
     return num_cherries // 2 * 5
    else:
       return 0 

    

def get_score(cherries):
    """Returns a player's total score based on their cards of each type."""
    cherry_score = get_cherry_score(cherries)
    return cherry_score

player1_score = get_score(20)

print("Scores: p1=" + str(player1_score))