data_one = """/dev/sda :
                /dev/sda1 other, 21686148-6449-6e6f-744e-656564454649
                /dev/sda2 other, ext3, mounted on /boot
                /dev/sda3 other, LVM2_member
              /dev/sdb other, unknown
              /dev/sdc :
                /dev/sdc1 other, xfs, mounted on /srv/node/disk0
              /dev/sdd :
                /dev/sdd1 other, xfs, mounted on /srv/node/disk1
              /dev/sde other, LVM2_member
              /dev/sdf other, unknown
"""


data_two = """WARNING:ceph-disk:Old blkid does not support ID_PART_ENTRY_* fields, trying sgdisk; may not correctly identify ceph volumes with dmcrypt
/dev/sda :
 /dev/sda1 other, 21686148-6449-6e6f-744e-656564454649
 /dev/sda2 other, ext3, mounted on /boot
 /dev/sda3 other, LVM2_member
/dev/sdb :
 /dev/sdb1 ceph data, active, cluster ceph, osd.5, journal /dev/sdd1
/dev/sdc :
 /dev/sdc1 ceph data, active, cluster ceph, osd.8, journal /dev/sdd2
/dev/sdd :
 /dev/sdd1 ceph journal, for /dev/sdb1
 /dev/sdd2 ceph journal, for /dev/sdc1
/dev/sde :
 /dev/sde1 ceph data, active, cluster ceph, osd.3, journal /dev/sdg2
/dev/sdf :
 /dev/sdf1 ceph data, active, cluster ceph, osd.1, journal /dev/sdg1
/dev/sdg :
 /dev/sdg1 ceph journal, for /dev/sdf1
 /dev/sdg2 ceph journal, for /dev/sde1
"""


def parse_data(data):
    jdm = ddm = dict()
    for l in data.split('\n'):
        if " :" in l:
            device = l.split(" :")[0]
            ddm[device] = list()
            jdm[device] = list()
        elif "ceph journal" in l:
            jdm[device].append(l)
        elif "ceph data" in l:
            ddm[device].append(l)

    print(jdm)
    print(ddm)


if __name__ == "__main__":
    parse_data(data_two)
