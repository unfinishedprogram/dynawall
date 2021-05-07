pkill -f 'wallinit.py'
for arg in "$@"
do
    python ./wallinit.py "$arg" &
done
