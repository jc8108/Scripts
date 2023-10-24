#!/bin/bash
# remove no numbers
echo 'Usage: ./betterlist.sh passwordlist.txt'
echo 'Removing everything shorter than 8 characters or missing special characters or missing numbers from wordlist.'
cp $1 better-list.txt
sed -ri '/^.{,7}$/d' better-list.txt
sed -ri '/[!-/:-@[-`{-~]+/!d' better-list.txt
sed -ri '/[0-9]+/!d' better-list.txt
echo 'better-list.txt ready.'
# can do | grep [[:upper:]] if you need uppercase as well. 
