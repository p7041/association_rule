class arules():
    def __init__(self,minSupport=0.02,minConf=0.3):
        self.minSupport = minSupport
        self.minConf = minConf
        self.L = None
        self.supportData = None 
                 
    def createC1(self,dataset):
        C1 = []
        for transaction in dataset:
            for item in transaction:
                if [item] not in C1:
                    C1.append([item])
        C1.sort()
        return list(map(frozenset,C1))
    
    def scanD(self,D, Ck, minSupport):
        ssCnt = {}
        for tid in D:
            for can in Ck:
                if can.issubset(tid):
                    if can not in ssCnt.keys():
                        ssCnt[can] = 1
                    else:
                        ssCnt[can] += 1
        numitems = float(len(D))
        retList = []
        supportData = {}
        for key in ssCnt:
            support = ssCnt[key] / numitems
            if support >= minSupport:    
                retList.insert(0,key)
            supportData[key] = support
        return retList, supportData
                        
    def aprioriGen(self,Lk, k):
        retList = []
        lenLk = len(Lk)
        for i in range(lenLk):
            for j in range(i+1,lenLk):
                temp = []
                temp.append(Lk[i] | Lk[j])
                temp.sort()
                if (temp[0] not in retList) and (len(temp[0])==k):
                    retList.extend(temp)
        return retList
    
    def apriori(self, dataSet):
        C1 = self.createC1(dataSet)
        D = list(map(set,dataSet))
        L1, supportData = self.scanD(D, C1, self.minSupport)
        L = [L1]
        k = 2
        while (len(L[k-2]) > 0):
            Ck = self.aprioriGen(L[k-2],k)
            Lk, supK = self.scanD(D, Ck, self.minSupport)
            supportData.update(supK)
            L.append(Lk)
            k += 1
        self.L = L ; self.supportData = supportData
    
    def generateRules(self):
        bigRuleList = []
        for i in range(1,len(self.L)):
            for freqSet in self.L[i]:
                H1 = [frozenset([item]) for item in freqSet]
                if i > 1:
                    self.rulesFromConseq(freqSet, H1, self.supportData, bigRuleList, self.minConf)
                else:
                    self.calcConf(freqSet, H1, self.supportData, bigRuleList, self.minConf)
        return bigRuleList
    
    def calcConf(self,freqSet, H, supportData, brl, minConf):
        prunedH=[]
        for conseq in H:
            conf = supportData[freqSet]/supportData[freqSet-conseq]
            lift = supportData[freqSet]/(supportData[freqSet-conseq]*supportData[conseq])
            if conf > minConf:
                print(freqSet-conseq,'--->',conseq, "conf: ",conf," lift: ",lift)
                brl.append((freqSet-conseq,conseq,conf,lift))
                prunedH.append(conseq)
        return prunedH
    
    def rulesFromConseq(self,freqSet, H, SupportData, brl, minConf):
        m = len(H[0])
        if (len(freqSet)>(m+1)):
            Hmp1 = self.aprioriGen(H,m+1)
            Hmp1 = self.calcConf(freqSet,Hmp1,SupportData,brl,)
            if (len(Hmp1) > 1):
                self.rulesFromConseq(freqSet, Hmp1, SupportData, brl, minConf)
            
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

    
        
    
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            