fr=open("input.txt", "r")

def create2Dmatrix(width, height):
    matrix=[]
    temp=[]
    for y in range (height):
        temp=[]
        for x in range (width):
            temp.append(0)
        matrix.append(temp)
    return matrix

def processfile():
    x=0
    y=0
    for row in fr:
        x=0
        for char in row:
            if char=="1":
                matrix[y][x]=1
            x+=1
        y+=1

def return_friends(x,y,matrix):
    count=0
    #matrix [y][x]
    # navrhem seriu ifov aby to fungovalo
    if y-1 >=0:
        if matrix [x-1] [y-1]==1 and x-1>=0 and y-1>=0:
            count +=1
        if matrix [x] [y-1]==1 and y-1>=0:
            count +=1
        if matrix [x+1] [y-1]==1 and x+1<=width and y-1>=0:
            count +=1
        if matrix [x-1] [y]==1 and x-1>=0:
            count +=1
        if matrix [x-1] [y+1]==1 and x-1>=0 and y+1<=height:
            count +=1
        if matrix[x+1] [y+1]==1 and x+1<=width and y+1<=height:

    return count




width, height=fr.readline().split(" ")
width=int(width)
height=int(height)

#vytvori 2 rozmerny zoznam plny nul
oldfield=create2Dmatrix(width, height)

#vytvori iny 2 rozmerny zoznam plny nul
newfield=create2Dmatrix(width, height)

#do prveho zoznamu nahodime jednotky zo suboru
processfile(oldfield)
