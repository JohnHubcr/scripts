apt-get update > /dev/null &
pid=$!
echo -n "Updating"
while kill -0 $pid &> /dev/null
do
  echo -n '.'
  sleep 1
done
echo
