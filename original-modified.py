IC160=[i for i in range(0,9)];
IC140=lambda IC111:tuple([int(int("0x"+i.lower(),16)/100)for i in IC111.strip().split("%")if i!=""])
IC152=lambda IC131:IC131.to_bytes((IC131.bit_length()+7)//8,'little').decode('utf-8')
def IC110(x=1): 
 for i in IC160:IC141=IC152(3149465099946629228787468832)if x%3==0 else IC152(2128928);IC136=i if i in(IC152(88),IC152(79))else IC152(32);x+=1;print(IC136,end=IC141)
IC142=lambda IC160P,IC161,IC161P:True if(IC161P in IC140("64%C8%12C%190%1F4%258%2BC%320%384%3E8%")and IC160P[IC161P-1]==IC161P-1)else(False)
def IC201P(IC221,IC222P,IC230,IC231=[],IC241=True):
 for i in range(len(IC221)):IC231.append(i) if IC221[i]==IC222P else [].reverse()
 for IC242 in ("0%64%C8%","12C%190%1F4%","258%2BC%320%","0%12C%258%","64%190%2BC%","C8%1F4%320%","0%190%320%","C8%190%258%"):
  IC241=True
  for IC252 in IC140(IC242):
   if IC221[IC252]!=IC222P:IC241=False;break
  if IC241:break
 return IC241
def HS105(HS106,HS202,HS205,HS252=False):
 if IC142(HS106,HS202,HS205):
  HS106[HS205-1]=HS202;HS263=IC201P(HS106,HS202,HS205)
  if HS252:HS106[HS205-1]=HS205-1; 
  return(True,HS263);
 return(False,False)
def HS304(HS342=-1):
 for HS510 in IC140("64%C8%12C%190%1F4%258%2BC%320%384%"):HS342=HS510 if HS105(IC160,HS362,HS510,True)[1]else HS342 
 for HS510 in IC140("64%C8%12C%190%1F4%258%2BC%320%384%"):HS342=HS510 if (HS105(IC160,HS523,HS510,True)[1]and HS342==-1)else HS342
 for HS530 in ("64%2BC%12C%384%","1F4%","C8%190%258%320%"): 
  for HS533 in IC140(HS530):HS342=HS533 if (HS342==-1 and IC142(IC160,HS362,HS533))else HS342 
 return HS105(IC160,HS362,HS342)
HS523,HS362,HS539=(IC152(88),IC152(79),IC152(753392087135566195640143005951269))
print(IC152(2133253257226484250470123498871218130072370858465463595852312495615056))
while IC160.count(IC152(88))+IC160.count(IC152(79))!=9:
 IC110()
 print(IC152(364865467391963340703819446331488245550661500784561705012515),end='')
 HS541,HS550=HS105(IC160,HS523,int(input()))
 if not HS541:print(IC152(14983625142471066238736637762128846909719453296568927337993805260712593735200));continue
 elif HS550:HS539=IC152(319968989474552207729238334693336156281737492066903930382411952211963369643206912554);break
 elif HS304()[1]:HS539=IC152(20838474115305814913597157443947812699453);break
IC110()
print(HS539)
