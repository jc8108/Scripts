wget $1/robots.txt
cat robots.txt | grep "Disallow:" | cut -d " " -f2 | sed -e 's!/var/www!!' | sed -e 's!/wordpress!!' > dirs.txt
rm robots.txt
cat dirs.txt
echo -e "\ndirs.txt available in current directory.\n"
read -p "Would you like to open all in Firefox? " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    while read line; do
        firefox --new-tab $1"$line"
done < dirs.txt
fi
