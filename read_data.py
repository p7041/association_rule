def readCSV():
    fr = open("C:\\Users\\e1175640\\Desktop\\RP\\Projects\\trans.csv")
    trans = {}
    for line in fr.readlines():
        curline = line.strip().split(',')
        if curline[0] not in trans.keys():
            trans[curline[0]] = [curline[1]]
        else:
            temp=[]
            temp.extend(trans[curline[0]])
            temp.append(curline[1])
            trans[curline[0]] = temp             
    itemList = [item for item in trans.values()] 
    return itemList
