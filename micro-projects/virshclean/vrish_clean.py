import subprocess
import sys


def delete(skip_patterns=list(), debug=False):
    try:
        process = \
            subprocess.Popen(["virsh", "vol-list", "--pool=default"],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        output, error = process.communicate()
        vmlines = output.split('\n')[2:]
        for line in vmlines:
            if line.strip():
                volume_info = line.split()
                matched_pattern = can_skip(volume_info[0], skip_patterns)
                if matched_pattern:
                    print('Skipping deletion of: %s as pattern %s matched' % (volume_info[0], matched_pattern))
                else:
                    if debug:
                        print('Asked for deletion of: %s but not doing so because of debug mode' % (volume_info[0]))
                    else:
                        process = \
                            subprocess.Popen(["virsh", "vol-delete", "--pool=default", volume_info[0]],
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
                        output, error = process.communicate()
    except Exception as e:
        print('Failed to clean VMs as per provided pattern')


def can_skip(element, patterns):
    for p in patterns:
        if p in element:
            return p
    return None

if __name__ == "__main__":
    skip_patterns = [
        'build-vagrant_build-hlinux',
        'hlinuxbox_vagrant_box_image',
        'persistent-ccache'
    ]
    delete(skip_patterns, True)