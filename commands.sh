# Author: Danique van der Wijk
# Date: 29-03-2021

# The command to go to the right directory
cd /net/corpora/twitter2/Tweets/2021/02

# The command to get the tweets containing the string 'elfstedentocht' with user.location per day
# Where [DAY] is the day in numbers (for example: feb 01 == 01, so you get 20210201:*out.gz)
zless 202102[DAY]:*.out.gz | /net/corpora/twitter2/tools/tweet2tab -i text user.location | grep -va '^RT' | grep -i 'Elfstedentocht'

# The command to count the lines of the textfiles in a directory
cat *.txt | wc -l

# The command to count the lines of a specific document
# where [DOC] is the name of the document before the extension .txt
cat [DOC].txt | wc -l
