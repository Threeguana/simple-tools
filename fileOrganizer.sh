#!/system/bin/sh

TARGET_DIR="."

cd "$TARGET_DIR" || exit

for file in *; do
    
    if [ -f "$file" ] && [ "$file" != "${0##*/}" ]; then
        ext="${file##*.}"
        
        if [ "$ext" = "$file" ]; then
            ext="unknown"
        fi
        
        [ -d "$ext" ] || mkdir -p "$ext"
        mv "$file" "$ext/"
    fi
done
