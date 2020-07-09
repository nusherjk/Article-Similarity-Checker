import sys



#sys.setrecursionlimit(1500)
class TNode:

    def __init__(self,value,word):
        self.value = value
        self.word = word
        self.cwc = 1
        self.right = None
        self.left = None



    def insert(self,data,word,index):

        if(data> self.value):
            if (self.right):
                return self.right.insert(data,word,index)

            else:
                self.right = TNode(data,word)
                self.cwc = self.cwc + 1
              #  self.right.indexlist.addToEnd(index)
                return True
        elif(data==self.value):
            self.cwc += 1
            #self.indexlist.addToEnd(index)

        else:
            if(self.left):
                return self.left.insert(data,word,index)
            elif (data == self.value):
                self.cwc += 1
                self.counter = self.counter + 1
            else:
                self.left= TNode(data,word)
                self.cwc+=1
                return True

    def printTree(self,total_word):

        if self.right:
            self.right.printTree(total_word)

        if self.left:
            self.left.printTree(total_word)
        print(str(self.word), end=' ')


        #tw = self.indexlist.listprint()
       # print(tw/total_word)

    def wordfreq(self,value):
            if(value == self.value):
                return self.cwc
            elif(value>self.value):
                if(self.right):
                    return self.right.wordfreq(value)
                else:
                    return 0

            elif(value<self.value):
                if(self.right):
                    return self.left.wordfreq(value)
                else:
                    return 0
            else:
                return 0


class Tree:

    def __init__(self):
        self.root = None
        self.word = None
        self.wc=0
        self.tncwc=0
        self.tlist = []



    def insert(self, data,word,index):
        self.tlist.append(self.word)
        self.wc = self.wc+1
        if(self.root):
           return  self.root.insert(data, word, index)
        else:
            self.root = TNode(data, word)
      #    self.root.indexlist.addToEnd(index)

    def printTree(self):
        if(self.root):
            s = self.root.printTree(self.wc)
        return s

    def printnumber(self):
        return self.wc

    def wordfreq(self,value):
        if(self.root):
            self.tncwc =  self.root.wordfreq(value)
            return self.tncwc/self.wc
        else:
            return 0
    def listOfwords(self):
        return self.tlist



