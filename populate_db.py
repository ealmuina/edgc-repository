from model import *

if __name__ == '__main__':
    db.connect()
    db.drop_tables([Task, Domain])
    db.create_tables([Task, Domain])

    t1 = Task(
        cpu_intensity=2,
        com_intensity=1,
        io_intensity=0,
        kernel='kernel/kernel-0.txt',
        input='input/in-0.tar.gz',
        output='output/out-0.tar.gz',
        pack='scripts/pack-0.sh',
        unpack='scripts/unpack-0.sh'
    )
    t1.save()
