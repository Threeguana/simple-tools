#!/system/bin/sh

# ===========================================================
#  File Organizer - Android Shell
# ===========================================================

# Gunakan folder saat ini
TARGET_DIR="."

cd "$TARGET_DIR" || exit

for file in *; do
    # Pastikan itu adalah file (bukan folder) dan bukan script ini sendiri
    if [ -f "$file" ] && [ "$file" != "${0##*/}" ]; then
        # Ambil ekstensi file
        ext="${file##*.}"
        
        # Jika file tidak memiliki ekstensi
        if [ "$ext" = "$file" ]; then
            ext="unknown"
        fi
        
        # Buat folder jika belum ada, lalu pindahkan
        [ -d "$ext" ] || mkdir -p "$ext"
        mv "$file" "$ext/"
    fi
done
