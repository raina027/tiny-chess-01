import json,os,urllib.request as w
H=os.environ["MAKEFUN_ENV_URL"]
def Q(a,b):
 try:return json.load(w.urlopen(w.Request(H+a,data=json.dumps(b).encode(),headers={"content-type":"application/json"})))
 except:raise SystemExit
V=[0,100,320,330,500,1000,0]
ND=(33,31,18,14,-14,-18,-31,-33)
RD=(16,-16,1,-1)
BD=(17,15,-15,-17)
DD=(ND,BD,RD,RD+BD,RD+BD)
CR={0:2,7:1,112:8,119:4}
M=10**5
I=10**6
N=60000
T=['````\x92\x92\x92\x92jjt~eejy```te[V`ejjL````','.8BB8L``B`joBeotB`otBejo8L`e.8BB','LVVVV```V`ejVeejV`jjVjjjVe``LVVV','````ejjj[```[```[```[```[``````e','LVV[V```V`ee[`ee``eeVeeeV`e`LVV[','B88.B88.B88.B88.LBB8VLLLtt``t~j`']
def h(s):return[ord(s[(i//8)*4+min(i%8,7-i%8)])-96 for i in range(64)]
G=[0]+[h(s)for s in T]
G[5][39:54:7]=[-5,0,0]
U=[]
def f(n):
 global B,S,C,E,W,K
 B=[0]*128;d=n.split();r=7;i=0
 for w in d[0]:
  if w=="/":r-=1;i=0
  elif w.isdigit():i+=int(w)
  else:
   q=r*16+i;p="PNBRQK".index(w.upper())+1
   if w.islower():p=-p
   B[q]=p
   if abs(p)==6:
    if p>0:W=q
    else:K=q
   i+=1
 S=1-2*(d[1]=="b")
 C=sum(1<<"KQkq".index(c)for c in d[2]if c in"KQkq")
 E=ord(d[3][0])-97+(int(d[3][1])-1)*16 if d[3]!="-" else-1
def A(q,t):
 for v,o,s in((1,(-17*t,-15*t),0),(2,ND,0),(6,RD+BD,0),(4,RD,1),(3,BD,1)):
  for d in o:
   u=q+d
   while not(u&0x88):
    p=B[u]
    if p:
     if p==v*t or s and p==5*t:return 1
     break
    if not s:break
    u+=d
 return 0
def g(c=0):
 m=[]
 for f,p in enumerate(B):
  if f&0x88 or not p or p*S<0:continue
  n=abs(p)
  if n==1:
   d=16*S
   r=7*(S>0)
   for e in(d-1,d,d+1):
    t=f+e
    if t&0x88:continue
    q=B[t]
    if e==d:
     if q or(c and(t>>4)!=r):continue
    elif not(q and q*S<0)and not(t==E and E>=0):continue
    if(t>>4)==r:m+=[f|(t<<7)|(v<<14)for v in(5,4,3,2)]
    else:
     m.append(f|(t<<7))
     if e==d and(f>>4)==(1 if S>0 else 6):
      u=f+2*d
      if B[u]==0:m.append(f|(u<<7))
  else:
   for d in DD[n-2]:
    t=f+d
    while not(t&0x88):
     q=B[t]
     if q==0:
      if not c:m.append(f|(t<<7))
     else:
      if q*S<0:m.append(f|(t<<7))
      break
     if n==2 or n==6:break
     t+=d
   if n==6 and not c:
    y0=W if S>0 else K
    b0=1 if S>0 else 4
    for s2 in(1,-1):
     if C&((1 if s2>0 else 2)*b0)and B[y0+3*s2 if s2>0 else y0-4]==4*S and all(B[y0+i*s2]==0 for i in(1,2,3)if s2<0 or i<3)and not any(A(y0+i*s2,-S)for i in(0,1,2)):m.append(f|((y0+2*s2)<<7))
 return m
def k(m):
 global S,C,E,W,K
 f=m&127
 t=(m>>7)&127
 r=(m>>14)&7
 p=B[f]
 q=B[t]
 s=t
 if abs(p)==1 and t==E and q==0:
  s=t-16*S
  q=B[s]
  B[s]=0
 U.append((f,t,p,q,s,C,E,W,K))
 B[t]=r*S if r else p
 B[f]=0
 if abs(p)==6:
  if S>0:W=t
  else:K=t
  if abs(t-f)==2:Rk(t+1 if t>f else t-2,t-1 if t>f else t+1)
  C&=~(3 if S>0 else 12)
 C&=~CR.get(f,0);C&=~CR.get(t,0)
 E=(f+t)//2 if abs(p)==1 and abs(t-f)==32 else-1
 S=-S
def Rk(a,b):
 B[b]=B[a];B[a]=0
def v():
 global S,C,E,W,K
 f,t,p,q,s,C,E,W,K=U.pop()
 S=-S
 B[t]=0
 B[f]=p
 if q:B[s]=q
 if abs(p)==6 and abs(t-f)==2:Rk(t-1 if t>f else t+1,t+1 if t>f else t-2)
def e():
 m=0
 for q in range(128):
  p=B[q]
  if q&0x88 or not p:continue
  a=abs(p)
  j=(7-(q>>4)if p>0 else q>>4)*8+(q&7)
  m+=(V[a]+G[a][j])*(p//a)
 return m*S
def o(m):
 return sorted(m,key=lambda z:-V[abs(B[z>>7&127])])
def s(a,b,d,p):
 global n,J
 n+=1
 if n>N:raise StopIteration
 if d<=0:
  t=e()
  if t>=b:return b
  if t>a:a=t
  m=o(g(1))
 else:m=o(g())
 r=-I
 l=0
 for w in m:
  k(w)
  if A(W if S<0 else K,S):
   v()
   continue
  l+=1
  j=-s(-b,-a,d-1,p+1)
  v()
  if j>r:
   r=j
   if p==0:J=w
  if j>a:
   a=j
   if a>=b:break
 if d<=0:return a
 if l==0:return-M+p if A(W if S>0 else K,-S) else 0
 return r
def b(w,l):
 global n,Y
 f(w)
 Y=l[0]
 n=0
 for d in range(1,17):
  try:s(-I,I,d,0);Y=J
  except StopIteration:break
 if isinstance(Y,int):
  i=Y&127;j=(Y>>7)&127;k=(Y>>14)&7
  Y="".join(chr(97+(x&7))+str((x>>4)+1)for x in(i,j))
  if k:Y+="nbrq"[k-2]
 return Y
def main():
 while 1:
  g=Q("/game",{})
  if g["status"]!="your_move":break
  l=g["legal_moves"];v=g["game"]
  z=b(g["fen"],l)
  try:g=Q("/move",{"game":v,"move":z})
  except SystemExit:pass
__name__=="__main__"and main()
