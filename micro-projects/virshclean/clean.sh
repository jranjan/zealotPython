var=$(virsh vol-list --pool=default | grep padawan | awk '{print $1}')
for vm in $var
do
        virsh vol-delete --pool=default $vm
done
