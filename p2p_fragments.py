from mpi4py import MPI
import numpy as np
from itertools import islice

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


total_elements = 1000
array = np.arange(total_elements)  
array = iter(array)

chunk_size = 250
new_start = start = 0
new_end = end = 250
if rank==0:
    print(end)
    while start<1002:
        comm.send([new_start, new_end], dest=1)
        indices0 = comm.recv(source=1)
        if len(indices0)==0: break
        start = indices0[0]
        end = indices0[1]
        new_start = end+1
        new_end = new_start+249
        print('The rank', rank, indices0)
        print('rank 0 sent: ', new_start, new_end)
    print('node 0 is at rest')
else: 
    print(end)
    while True:
        indices = comm.recv(source=0)
        print('rank 1 receives: ', indices)
        start = indices[0]
        end = indices[1]
        print(end)
        if start>1000:
            comm.send([],dest=0)
            break
        else:
            new_start = end+1
            new_end = new_start+249
            comm.send([new_start, new_end], dest=0) 
            print('sent: ', new_start, new_end)
    print('node 1 is at rest')
'''
if rank==0:
    for i, data in enumerate(gather_data):
        print(f"Data from process {i}: {data}")  
'''
