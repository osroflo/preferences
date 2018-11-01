for i in *.png; do ext=${i##*.}; name=$(basename "$i" ".$ext" | tr '[a-z]' '[A-Z]').$ext; cp $i upper/$name; done
