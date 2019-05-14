from model import *

if __name__ == '__main__':
    db.connect()
    db.drop_tables([Task])
    db.create_tables([Task, Domain])

    tasks = [
        Task(
            cpu_intensity=2000,
            com_intensity=100,
            mem_intensity=2000000,
            kernel='kernel/kernel-0.txt',
            input='input/in-0.tar.gz',
            output='output/out-0.tar.gz',
            pack='scripts/pack-0.sh',
            unpack='scripts/unpack-0.sh'
        ),
        Task(
            cpu_intensity=2000,
            com_intensity=100,
            mem_intensity=2000000,
            kernel='kernel/kernel-0.txt',
            input='input/in-0.tar.gz',
            output='output/out-0.tar.gz',
            pack='scripts/pack-0.sh',
            unpack='scripts/unpack-0.sh'
        )
    ]

    for t in tasks:
        t.save()
