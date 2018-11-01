find . -iname "*.png" -type f -exec identify -format '%i %wx%h\n' '{}' \; | grep '75x75'
