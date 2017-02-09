class Case():
    def __init__(self,x,y):
        self.x = x*cols
        self.y = y*lignes
        self.posx = x
        self.posy = y
        self.murs = [1,1,1,1]
        self.visited = 0
        self.twice = 0
    
    def show(self):
        if self.visited == 1:
            stroke(0,255,0)
        else:
            stroke(255,0,0)
        if self.murs[0] == 1:
            line(self.x,self.y,self.x+cols,self.y)
        if self.murs[1] == 1:
            line(self.x+ cols,self.y,self.x+cols,self.y+lignes) 
        if self.murs[2] == 1:
            line(self.x,self.y+lignes,self.x+cols,self.y+lignes)
        if self.murs[3] == 1:
            line(self.x,self.y,self.x,self.y+lignes)

            
        
    def highlight(self):
        noStroke()
        fill(255,128,0)
        rect(self.x,self.y,cols,lignes)
        
        
    def checkVoisins(self):
        self.voisins = []
        
        if self.posx > 0: 
            if grille[((self.posx-1) + self.posy * nbCase)].visited == 0:
                self.voisins.append(grille[((self.posx-1) + self.posy * nbCase)])
        if self.posx < nbCase-1:
            if grille[((self.posx+1) + self.posy * nbCase)].visited == 0:
                self.voisins.append(grille[((self.posx+1) + self.posy * nbCase)])
        
        if self.posy > 0:
            if grille[((self.posx) + (self.posy-1) * nbCase)].visited == 0:
                self.voisins.append(grille[((self.posx) + (self.posy-1) * nbCase)])
                
        if self.posy < nbCase -1:
            if grille[((self.posx) + (self.posy+1) * nbCase)].visited == 0:
                self.voisins.append(grille[((self.posx) + (self.posy+1) * nbCase)])
        

                             
                                        
def RemoveWalls(current,next):
    x = current.posx - next.posx
    
    if x ==1:
        current.murs[3] = 0
        next.murs[1] = 0
    elif(x == -1):
        current.murs[1] = 0
        next.murs[3] = 0
        
    y = current.posy - next.posy
    
    if y ==1:
        current.murs[0] = 0
        next.murs[2] = 0
    elif(y == -1):
        current.murs[2] = 0
        next.murs[0] = 0
        
                                                                                                                        


def setup():
    global height, width,cols,lignes,current,stack,grille,nbCase
    nbCase = 200
    size(800,800)
    background(51)
    cols = floor(width / nbCase)
    lignes = floor(height / nbCase)
    grille = [0]*(nbCase**2)
    
    for x in range(nbCase):
        for y in range(nbCase):
            pos = x + y * nbCase
            grille[pos] = Case(x,y)
            grille[pos].show()
            
    current = grille[0]
    stack = [current]
    

    
def draw():
    global current
    background(51)
    for i in range(nbCase):
        for j in range(nbCase):
            pos = i + j * nbCase
            grille[pos].show()  
            
    noStroke()
    fill(0,255,0)
    rect(grille[nbCase-1 + (nbCase-1) * nbCase].x,grille[nbCase-1 + (nbCase-1) * nbCase].y,cols,lignes)    
    while len(stack) != 0:
        current.visited = 1
        current.highlight()
        #STEP 1
        current.checkVoisins()
    
        if len(current.voisins) > 0:
            
            stack.append(current)
            next = current.voisins[int(random(len(current.voisins)))]       
            RemoveWalls(current,next)
            current = next
    
        elif len(stack) > 0:
            current = stack.pop()
            current.twice = 1

    print('fini')
    
    background(51)
    for i in range(nbCase):
        for j in range(nbCase):
            pos = i + j * nbCase
            grille[pos].show() 
    noLoop()
            
      
        
    
     
        
