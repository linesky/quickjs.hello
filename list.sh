cat $1 | grep -v "rror" | grep -v "messages"| grep -v "No such file" | grep -v -e '^$'
