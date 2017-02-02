# Copyright (c) 2016-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE_camera_ctl file in the root directory of this subproject.

#!/bin/bash

mount -o noatime /dev/md127 /media/snoraid
for DEV in {sd{a,b},md127}
do
  echo "device: ${DEV}"
  echo noop > /sys/block/${DEV}/queue/scheduler
  echo 0 > /sys/block/${DEV}/queue/rotational
  echo 1024 > /sys/block/${DEV}/queue/nr_requests
done
for CPUFREQ in /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor; do [ -f $CPUFREQ ] || continue; echo -n performance > $CPUFREQ; done
