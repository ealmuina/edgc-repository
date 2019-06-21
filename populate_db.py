from model import *

if __name__ == '__main__':
    db.connect()
    db.drop_tables([Task, Domain])
    db.create_tables([Task, Domain])
    tasks = [
        Task(
            cpu_intensity=0,
            com_intensity=0,
            mem_intensity=0,
            kernel='kernel/dlkernel1.so',
            parameters='5000:2:1:0:2.500000:500',
            output='output/out-1.tar.gz',
            pack='scripts/pack-1.sh',
            unpack='scripts/unpack-1.sh'
        ),
        Task(
            cpu_intensity=0,
            com_intensity=0,
            mem_intensity=0,
            kernel='kernel/dlkernel2.so',
            parameters='10000:2:1:0:2.500000:3000',
            output='output/out-2.tar.gz',
            pack='scripts/pack-2.sh',
            unpack='scripts/unpack-2.sh'
        ),
        Task(
            cpu_intensity=0,
            com_intensity=0,
            mem_intensity=0,
            kernel='kernel/dlkernel3.so',
            parameters='3500:2:1:0:2.500000:500',
            # input='input/nd6k.dat',
            output='output/out-3.tar.gz',
            pack='scripts/pack-3.sh',
            unpack='scripts/unpack-3.sh'
        ),
        Task(
            cpu_intensity=0,
            com_intensity=0,
            mem_intensity=0,
            kernel='kernel/dlkernel4.so',
            parameters='5000:2:1:0:2.500000:500',
            output='output/out-4.tar.gz',
            pack='scripts/pack-4.sh',
            unpack='scripts/unpack-4.sh'
        ),
    ]

    for t in tasks:
        t.save()
