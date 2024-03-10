from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank==0:
    data={
        'a':7,
        'b':3.14
    }
    req = comm.isend(data, dest=1, tag=11)
    print('ps 0 sent a message: ', data)
    req.wait()
    print(req.test())
elif rank==1:
    req = comm.irecv(source=0, tag=11)
    data = req.wait()
    print('ps 1 received a message: ', data)
    print(req.test())
else:
    print('ps ', rank, ' did nothing')
