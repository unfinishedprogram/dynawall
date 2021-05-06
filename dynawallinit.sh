pkill -f 'wallinit.py'
for arg in "$@"
do
    python ~/.dynawall/wallinit.py "$arg" &
done