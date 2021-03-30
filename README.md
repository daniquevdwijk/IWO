# On thin ice
A study about positive and negative tweets regarding the possibility of an Elfstedentocht in 2021

## Prerequisites
The code in this repository needs to be run a computer with access to the Karora server of the Faculty of Arts at the University of Groningen. The user must also be able to run Python programs on the computer.

## Running the code
To get the results, we ran the second line of code in the shell script: commands.sh. This shell script will not work as a normal shell script, because it is not written in that way. The second line of code must be run on the first eight (8) days of Febraury 2021. The user has to put the output in a textfile manually and save the textfile.
After getting the tweets, the user must remove the tweets with an empty user.location or with a user location that is equal to, for example, 'The Netherlands'. This can be done with locprog.py. The command is: <br />
`python3 locprog.py [normaltweets].txt > [newtweets].txt` <br />
Where `[normaltweets].txt` is the name of the file with the extracted tweets from karora and `[newtweets].txt` is the output file. The user can decide the names of the file as long as the input file is an existing file in the repository. <br />
To remove whitelines in the file, the user can use delwhite.py. This program deletes whitelines in the given textfile. The command is: <br />
`python3 delwhite.py [withwhite].txt > [withoutwhite].txt` <br />
Where `[withwhite].txt` is the file with whitelines. `[withoutwhite].txt` is the output file. The user can decide the names of the files as long as the input file is an existing file in the repository.

## Info
Date: 30-03-2021 <br />
Author: Danique van der Wijk
