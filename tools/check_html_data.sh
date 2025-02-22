#!/bin/bash
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
rc=0
for file in $(find "$SCRIPT_DIR/.." -type f -name "*.html"); do
    # Extract carousel IDs from the file and check for duplicates
    carousels=$(grep -o 'id="carousel[0-9]*"' "$file" | sort)
    duplicates=$(echo "$carousels" | uniq -d)

    if [ -n "$duplicates" ]; then
        echo "Error: Duplicate carousel IDs found in $file:"
        echo "$duplicates"
        rc=$((rc + 1))
    fi

    # Extract data carousel IDs from the file and check for duplicates
    carousels=$(grep -o 'data-carousel="carousel[0-9]*"' "$file" | sort)
    duplicates=$(echo "$carousels" | uniq -d)

    if [ -n "$duplicates" ]; then
        echo "Error: Duplicate data carousel IDs found in $file:"
        echo "$duplicates"
        rc=$((rc + 2))
    fi

done
exit $rc