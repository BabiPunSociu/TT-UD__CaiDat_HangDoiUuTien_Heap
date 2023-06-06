# Ngay 15/10/2022
# Cài đặt hàng đợt ưu tiên

from ast import main


class PQ:
    def __init__(self): self.buf=[]
    def qsize(self): return len(self.buf)
    def top(self): return self.buf[0]
    def put(self, x): 
        self.buf.append(x)
        p=len(self.buf)-1
        while p>0 and self.buf[(p-1)//2]<self.buf[p]:
            self.buf[(p-1)//2],self.buf[p] = self.buf[p], self.buf[(p-1)//2]    # swap
            p=(p-1)//2
    def get(self):
        res=self.buf[0]
        self.buf[0] = self.buf[-1]
        self.buf.pop()
        self.heapy(0)
        return res
    def heapy(self, k):
        if 2*k+1>=len(self.buf): return
        p=2*k+1
        if p+1< len(self.buf)  and self.buf[p]<self.buf[p+1]: p+=1
        if self.buf[k]<self.buf[p]:
            self.buf[k], self.buf[p] = self.buf[p],self.buf[k]
            self.heapy(p)

if __name__ == "__main__":
    Q=PQ()
    for x in [253,125,28,11,2001,10,2002]: Q.put(x)

    while Q.qsize():
        print( Q.get(), end=" ")


