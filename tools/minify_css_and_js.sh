#!/bin/bash
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

# CSS
CSS_DIR="$SCRIPT_DIR/../stylesheets"
INPUT_CSS=$(cat $CSS_DIR/style-max.css)
OUTPUT_CSS="$CSS_DIR/style.css"

curl -X POST -s --data-urlencode "input=$INPUT_CSS" https://www.toptal.com/developers/cssminifier/api/raw > "$OUTPUT_CSS"

if [ $? -eq 0 ]; then
    if grep "errors" $OUTPUT_CSS; then
        echo "Error: CSS minification failed."
        echo "$OUTPUT_CSS"
        exit 1
    fi
    echo "CSS minification successful. Output saved to $CSS_DIR/$OUTPUT_CSS."
else
    echo "Error: CSS minification failed."
    echo "$OUTPUT_CSS"
    exit 2
fi

# JS
JS_DIR="$SCRIPT_DIR/../js"
INPUT_JS=$(cat $JS_DIR/carousel-max.js)
OUTPUT_JS="$JS_DIR/carousel.js"

curl -X POST -s --data-urlencode "input=$INPUT_JS" https://www.toptal.com/developers/javascript-minifier/api/raw > "$OUTPUT_JS"
if [ $? -eq 0 ]; then
    if grep "errors" $OUTPUT_JS; then
        echo "Error: JS minification failed."
        echo "$OUTPUT_JS"
        exit 3
    fi
    echo "JS minification successful. Output saved to $OUTPUT_JS."
else
    echo "Error: JS minification failed."
    echo "$OUTPUT_JS"
    exit 4
fi