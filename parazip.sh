# Parallel (multi threaded) bzip2 of a directory with lowest priority CPU/IO scheduling.
# Utilizes all cpu cores and detaches into background, will syslog when it's done.
# Originally written by (c) 2019 Chotaire - https://git.chotaire.net/chotaire/parazip

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

if ([ "$1" = "" ] || [ "$1" = "help" ] || [ "$1" = "--help" ])
then
        echo "parazip <dir> (where <dir> is a directory name found in the current directory)"
        echo "parazip install (will check for dependancies and install if not available)"

elif [ "$1" = "install" ]
then
        if ((grep -q -i "centos" /etc/os-release) || (grep -q -i "fedora" /etc/os-release) || (grep -q -i "rhel" /etc/os-release)) then
                if ! rpm -qa | grep -qw util-linux then
                        yum install util-linux -y
                fi
                if ! rpm -qa | grep -qw coreutils then
                        yum install coreutils -y
                fi
                if ! rpm -qa | grep -qw pbzip2 then
                        yum install pbzip2 -y
                fi
        else 
                echo "No Redhat-based operating system found. Please install dependancies manually."
        fi

else
        dirname=$(echo $1 | sed 's:/*$::')
        nohup bash -c "tar -c $dirname | pbzip2 -vc > $dirname.tar.bz2 ; logger -t parazip Finished." </dev/null &>/dev/null &
        sleep 1
        PID=`pgrep -f "pbzip2"`
        PID2=`pgrep -f "tar -c"`
        renice +20 $PID $PID2
        ionice -c 3 -p $PID $PID2
fi
