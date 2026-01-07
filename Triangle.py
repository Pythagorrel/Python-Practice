def equilateral(sides):
    if len(sides)!=3:
        return len(sides)==3
        
    if sides[0]==0:
        if sides[1]==0:
            if sides[2]==0:
                return 1==0 #silly way of writing return false
                
    ab = sides[0]+sides[1]
    bc = sides[1]+sides[2]
    ac = sides[0]+sides[2]

    

    if ab<sides[2]:
        return ab>sides[2]
    elif bc<sides[0]:
        return bc>sides[0]
    elif ac<sides[1]:
        return ac>sides[1]
        
    if sides[0]!=sides[1]:
        return 1==2
    elif sides[1]!=sides[2]:
        return 1==2
    elif sides[0]!=sides[2]:
        return 1==2
    
    return 1==1

def equilateral(sides):
    if len(sides)!=3:
        return len(sides)==3
        
    if sides[0]==0:
        if sides[1]==0:
            if sides[2]==0:
                return 1==0 #silly way of writing return false
                
    ab = sides[0]+sides[1]
    bc = sides[1]+sides[2]
    ac = sides[0]+sides[2]

    

    if ab<sides[2]:
        return ab>sides[2]
    elif bc<sides[0]:
        return bc>sides[0]
    elif ac<sides[1]:
        return ac>sides[1]
        
    if sides[0]!=sides[1]:
        return 1==2
    elif sides[1]!=sides[2]:
        return 1==2
    elif sides[0]!=sides[2]:
        return 1==2
    
    return 1==1

def scalene(sides):
    
    if len(sides)!=3:
        return len(sides)==3

    if sides[0]==0:
        if sides[1]==0:
            if sides[2]==0:
                return 1==0
                
    ab = sides[0]+sides[1]
    bc = sides[1]+sides[2]
    ac = sides[0]+sides[2]

    if ab<sides[2]:
        return ab>sides[2]
    elif bc<sides[0]:
        return bc>sides[0]
    elif ac<sides[1]:
        return ac>sides[1]

    if sides[0]==sides[1]:
        return 1==0
    elif sides[0]==sides[2]:
        return 1==0
    elif sides[1]==sides[2]:
        return 1==0
    return 1==1