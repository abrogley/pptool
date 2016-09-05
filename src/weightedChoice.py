def weightedChoice(choices):
    # Sum of all weights
    total = sum(w for c, w in choices)
    
    # Random number up to total
    r = random.uniform(0, total)
    
    # Select random number based on 
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"
    
def weightedPair(choicesInput):
    # Make a local copy of choices
    choices = list(choicesInput)
    
    # Get the first choice
    first = weightedChoice(choices)

    # Remove first choice from list
    ii = 0
    for c, w in choices:
        if c == first :
            #print("First choice was " + c.getCityName() + ", removing it for Second choice.")
            choices.pop(ii)
        ii += 1
    #print("New array length: " + str(len(choices)))
    # Select a new choice
    second = weightedChoice(choices)
    #print("   Second choice was " + second.getCityName())
    return [first, second]