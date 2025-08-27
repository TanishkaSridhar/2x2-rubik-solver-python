#cuboid rotation in appropriate to the move mentioned
def Fp(l):
    l1=[]
    for i in range(len(l)):
        if i==0:
           l1.append(l[1])
        elif i==1:
            l1.append(l[2])
        elif i==2:
            l1.append(l[3])
        elif i==3:
            l1.append(l[0])
        elif i==5:
            l1.append(l[14])
        elif i==6:
            l1.append(l[15])
        elif i==8:
            l1.append(l[17])
        elif i==11:
            l1.append(l[16])
        elif i==14:
            l1.append(l[11])
        elif i==15:
            l1.append(l[8])
        elif i==16:
            l1.append(l[5])
        elif i==17:
            l1.append(l[6])
        else:
            l1.append(l[i])
    return l1


def Dp(l):
    l1=[]
    for i in range(len(l)):
        if i==2:
            l1.append(l[10])
        elif i==3:
            l1.append(l[11])
        elif i==6:
            l1.append(l[2])
        elif i==7:
            l1.append(l[3])
        elif i==10:
            l1.append(l[22])
        elif i==11:
            l1.append(l[23])
        elif i==16:
            l1.append(l[17])
        elif i==17:
            l1.append(l[18])
        elif i==18:
            l1.append(l[19])
        elif i==19:
            l1.append(l[16])
        elif i==22:
            l1.append(l[6])
        elif i==23:
            l1.append(l[7])
        else:
            l1.append(l[i])
    return l1

def Up(l):
    l1=[]
    for i in range(len(l)):
        if i==0:
            l1.append(l[4])
        elif i==1:
            l1.append(l[5])
        elif i==4:
            l1.append(l[20])
        elif i==5:
            l1.append(l[21])
        elif i==8:
            l1.append(l[0])
        elif i==9:
            l1.append(l[1])
        elif i==12:
            l1.append(l[13])
        elif i==13:
            l1.append(l[14])
        elif i==14:
            l1.append(l[15])
        elif i==15:
            l1.append(l[12])
        elif i==20:
            l1.append(l[8])
        elif i==21:
            l1.append(l[9])
        else:
            l1.append(l[i])
    return l1

def Rp(l):
    l1=[]
    for i in range(len(l)):
        if i==1:
            l1.append(l[13])
        elif i==2:
            l1.append(l[14])
        elif i==8:
            l1.append(l[9])
        elif i==9:
            l1.append(l[10])
        elif i==10:
            l1.append(l[11])
        elif i==11:
            l1.append(l[8])
        elif i==13:
            l1.append(l[23])
        elif i==14:
            l1.append(l[20])
        elif i==17:
            l1.append(l[1])
        elif i==18:
            l1.append(l[2])
        elif i==20:
            l1.append(l[18])
        elif i==23:
            l1.append(l[17])
        else:
            l1.append(l[i])
    return l1


def Lp(l):
    l1=[]
    for i in range(len(l)):
        if i==0:
            l1.append(l[16])
        elif i==3:
            l1.append(l[19])
        elif i==4:
            l1.append(l[5])
        elif i==5:
            l1.append(l[6])
        elif i==6:
            l1.append(l[7])
        elif i==7:
            l1.append(l[4])
        elif i==12:
            l1.append(l[0])
        elif i==15:
            l1.append(l[3])
        elif i==16:
            l1.append(l[22])
        elif i==19:
            l1.append(l[21])
        elif i==21:
            l1.append(l[15])
        elif i==22:
            l1.append(l[12])
        else:
            l1.append(l[i])
    return l1

def F(l):
    l1=[]
    for i in range(len(l)):
        if i==0:
            l1.append(l[3])
        elif i==1:
            l1.append(l[0])
        elif i==2:
            l1.append(l[1])
        elif i==3:
            l1.append(l[2])
        elif i==5:
            l1.append(l[16])
        elif i==6:
            l1.append(l[17])
        elif i==8:
            l1.append(l[15])
        elif i==11:
            l1.append(l[14])
        elif i==14:
            l1.append(l[5])
        elif i==15:
            l1.append(l[6])
        elif i==16:
            l1.append(l[11])
        elif i==17:
            l1.append(l[8])
        else:
            l1.append(l[i])
    return l1

def Bp(l):
    l1=[]
    for i in range(len(l)):
        if i==4:
            l1.append(l[19])
        elif i==7:
            l1.append(l[18])
        elif i==9:
            l1.append(l[12])
        elif i==10:
            l1.append(l[13])
        elif i==12:
            l1.append(l[7])
        elif i==13:
            l1.append(l[4])
        elif i==18:
            l1.append(l[9])
        elif i==19:
            l1.append(l[10])
        elif i==20:
            l1.append(l[21])
        elif i==21:
            l1.append(l[22])
        elif i==22:
            l1.append(l[23])
        elif i==23:
            l1.append(l[20])
        else:
            l1.append(l[i])
    return l1

def U(l):
    l1=[]
    for i in range(len(l)):
        if i==0:
            l1.append(l[8])
        elif i==1:
            l1.append(l[9])
        elif i==4:
            l1.append(l[0])
        elif i==5:
            l1.append(l[1])
        elif i==8:
            l1.append(l[20])
        elif i==9:
            l1.append(l[21])
        elif i==12:
            l1.append(l[15])
        elif i==13:
            l1.append(l[12])
        elif i==14:
            l1.append(l[13])
        elif i==15:
            l1.append(l[14])
        elif i==20:
            l1.append(l[4])
        elif i ==21:
            l1.append(l[5])
        else:
            l1.append(l[i])
    return l1
                       
def L(l):
    l1=[]
    for i in range(len(l)):
        if i==0:
            l1.append(l[12])
        elif i==3:
            l1.append(l[15])
        elif i==4:
            l1.append(l[7])
        elif i==5:
            l1.append(l[4])
        elif i==6:
            l1.append(l[5])
        elif i==7:
            l1.append(l[6])
        elif i==12:
            l1.append(l[22])
        elif i==15:
            l1.append(l[21])
        elif i==16:
            l1.append(l[0])
        elif i==19:
            l1.append(l[3])
        elif i==21:
            l1.append(l[19])
        elif i==22:
            l1.append(l[16])
        else:
            l1.append(l[i])
    return l1





def D(l):
    l1=[]
    for i in range(len(l)):
        if i==2:
            l1.append(l[6])
        elif i==3:
            l1.append(l[7])
        elif i==6:
            l1.append(l[22])
        elif i==7:
            l1.append(l[23])
        elif i==10:
            l1.append(l[2])
        elif i==11:
            l1.append(l[3])
        elif i==16:
            l1.append(l[19])
        elif i==17:
            l1.append(l[16])
        elif i==18:
            l1.append(l[17])
        elif i==19:
            l1.append(l[18])
        elif i==22:
            l1.append(l[10])
        elif i==23:
            l1.append(l[11])
        else:
            l1.append(l[i])
    return l1

           
def R(l):
    l1=[]
    for i in range(len(l)):
        if i==1:
            l1.append(l[17])
        elif i==2:
            l1.append(l[18])
        elif i==8:
            l1.append(l[11])
        elif i==9:
            l1.append(l[8])
        elif i==10:
            l1.append(l[9])
        elif i==11:
            l1.append(l[10])
        elif i==13:
            l1.append(l[1])
        elif i==14:
            l1.append(l[2])
        elif i==17:
            l1.append(l[23])
        elif i==18:
            l1.append(l[20])
        elif i==20:
            l1.append(l[14])
        elif i==23:
            l1.append(l[13])
        else:
            l1.append(l[i])
    return l1

def B(l):
    l1=[]
    for i in range(len(l)):
        if i==4:
            l1.append(l[13])
        elif i==7:
            l1.append(l[12])
        elif i==9:
            l1.append(l[18])
        elif i==10:
            l1.append(l[19])
        elif i==12:
            l1.append(l[9])
        elif i==13:
            l1.append(l[10])
        elif i==18:
            l1.append(l[7])
        elif i==19:
            l1.append(l[4])
        elif i==20:
            l1.append(l[23])
        elif i==21:
            l1.append(l[20])
        elif i==22:
            l1.append(l[21])
        elif i==23:
            l1.append(l[22])
        else:
            l1.append(l[i])
    return l1

def U2(l):
    l1=U(l)
    l2=U(l1)
    return l2

def D2(l):
    l1=D(l)
    l2=D(l1)
    return l2

def F2(l):
    L1=F(l)
    L2=F(L1)
    return L2
def B2(l):
    l1=B(l)
    l2=B(l1)
    return l2
def L2(l):
    l1=L(l)
    l2=L(l1)
    return l2
def R2(l):
    l1=R(l)
    l2=R(l1)
    return l2
def U2p(l):
    l1=Up(l)
    l2=Up(l1)
    return l2
def D2p(l):
    l1=Dp(l)
    l2=Dp(l1)
    return l2
def F2p(l):
    l1=Fp(l)
    l2=Fp(l1)
    return l2
def B2p(l):
    l1=Bp(l)
    l2=Bp(l1)
    return l2
def L2p(l):
    l1=Lp(l)
    l2=Lp(l1)
    return l2
def R2p(l):
    l1=Rp(l)
    l2=Rp(l1)
    return l2

def y(l):
    l1=[]
    for i in range(len(l)):
        if i==0:
            l1.append(l[8])
        elif i==1:
            l1.append(l[9])
        elif i==2:
            l1.append(l[10])
        elif i==3:
            l1.append(l[11])
        elif i==4:
            l1.append(l[0])
        elif i==5:
            l1.append(l[1])
        elif i==6:
            l1.append(l[2])
        elif i==7:
            l1.append(l[3])
        elif i==8:
            l1.append(l[20])
        elif i==9:
            l1.append(l[21])
        elif i==10:
            l1.append(l[22])
        elif i==11:
            l1.append(l[23])
        elif i==12:
            l1.append(l[15])
        elif i==13:
            l1.append(l[12])
        elif i==14:
            l1.append(l[13])
        elif i==15:
            l1.append(l[14])
        elif i==16:
            l1.append(l[17])
        elif i==17:
            l1.append(l[18])
        elif i==18:
            l1.append(l[19])
        elif i==19:
            l1.append(l[16])
        elif i==20:
            l1.append(l[4])
        elif i==21:
            l1.append(l[5])
        elif i==22:
            l1.append(l[6])
        elif i==23:
            l1.append(l[7])
    return l1


def y2(l):
    l1=y(l)
    l2=y(l1)
    return l2
