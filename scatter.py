from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank==0:
    l = np.arange(102)
    k = 0
    while k <len(l):
        tmp = l[k:k+4]
        tmp_l = len(tmp)
        for i in range(tmp_l, size):
            tmp = np.append(tmp,0)
        for j in range(size):
            comm.send(tmp[j], dest=j)
        k+=4
    for j in range(size):
        comm.send('F', dest=j)
data = 0
while data!='F':
    data = comm.recv(source=0)
    if data =='F': break
    all_data = comm.gather((rank,data), root=1)
    if rank==1:
        print(all_data)

