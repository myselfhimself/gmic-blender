iconv -f ISO-8859-1 -t UTF-8//TRANSLIT gmic_filters.json -o gmic_filters.json2
cat gmic_filters.json2 | python3 -c 'import html, sys; [print(html.unescape(l), end="") for l in sys.stdin]' > gmic_filters.json3
rm gmic_filters.json2
jsonlint-php gmic_filters.json3 && mv gmic_filters.json3 gmic_filters_fixed.json
