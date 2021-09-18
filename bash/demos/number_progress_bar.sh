echo hey


echo -n "["
for ((i = 0 ; i <= 100 ; i+=6)); do
    echo -ne "###\e[s] ($i%)\e[u"
    sleep 0.5
done
echo
