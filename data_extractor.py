def txt2dic(txt):
    txt=[]
    para=[]
    line=[]
    word=""
    book=open(txt).read()
    for i in range(len(book)): 
        if book[i]=='.': 
            if(len(line)>0): 
                line.append(word) 
                word="" 
                line.append(book[i]) 
                para.append(line) 
            line=[] 
            continue 
        if book[i]=="\n": 
            if(len(para)>0): 
                line.append(word) 
                word="" 
                para.append(line) 
                line=[]             
                para.append("\n\n") 
                txt.append(para) 
            para=[] 
            continue 
        if book[i]==" ": 
            if(len(word)>0): 
                line.append(word) 
            word="" 
            continue 
        word+=book[i] 
    return book 

def dic2json(book):
    json=""
 #messed up here       
    return 

