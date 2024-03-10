FNAME=$1
set -x
python3 ocr_axis.py $FNAME > inexact.txt
python3 find_y_lines.py $FNAME | grep -v '^#' > exact.txt
python3 extract_red_values.py $FNAME > red.txt
grep maybey inexact.txt| python3 make_exact_y.py exact.txt > ex.txt
grep exactx inexact.txt >> ex.txt
python3 transform.py ex.txt red.txt | python3 interpolate.py /dev/stdin > measurements.txt
