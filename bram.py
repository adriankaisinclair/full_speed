#BRAM driver code for bram v0.42

veclen=2**8
vecoffs=2**19

def load_lut2(Z): # new stacked python functionality with new config
    wea=2**29
    memlen=2**9
    load=2**29
    sclr=2**31
    
    bram.write(4,wea)
    k=int(0)
    for i in range(0,memlen):
        #bram.write(4,1<<28)
        bram.write(0, k<<(32-9))
        bram.write(4,wea)
        for j in range(8):
            #print(f"{i}: {i<<16}") 
            bram.write(4,j<<19)
            bram.write(12,int(Z[i+j])) 
        bram.write(4,wea | 1<<27 )
            #bram.write(4,load)
        k+=1
        
    bram.write(4,0)     
    bram.write(0, 0)
    
def load_lut1(Z): # regular operation with one value, modified to work in new config
    wea=2**29
    memlen=2**9
    load=2**29
    sclr=2**31
    
    bram.write(4,wea)
    for i in range(memlen):
        bram.write(0, i<<(32-9))
        bram.write(4,wea)
        bram.write(12,int(Z[i]))
        bram.write(4,wea | 1<<27 )
    bram.write(4,0)     
    bram.write(0, 0)    

