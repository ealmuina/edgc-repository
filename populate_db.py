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
            output='output/out-1.tar.gz',
            pack='scripts/pack-1.sh',
            unpack='scripts/unpack-1.sh'
        ),
        Task(
            cpu_intensity=0,
            com_intensity=0,
            mem_intensity=0,
            kernel='kernel/dlkernel2.so',
            output='output/out-2.tar.gz',
            pack='scripts/pack-2.sh',
            unpack='scripts/unpack-2.sh'
        ),
        Task(
            cpu_intensity=0,
            com_intensity=0,
            mem_intensity=0,
            kernel='kernel/dlkernel3.so',
            output='output/out-3.tar.gz',
            pack='scripts/pack-3.sh',
            unpack='scripts/unpack-3.sh'
        ),
        Task(
            cpu_intensity=0,
            com_intensity=0,
            mem_intensity=0,
            kernel='kernel/dlkernel4.so',
            output='output/out-4.tar.gz',
            pack='scripts/pack-4.sh',
            unpack='scripts/unpack-4.sh'
        ),
    ]

    for t in tasks:
        t.save()
