hyperfine -i --shell=none --output=pipe --runs 3 --warmup 2 -n "Python - GIL" "python benchmark_test.py"
hyperfine -i --shell=none --output=pipe --runs 3 --warmup 2 -n "Python - No GIL" "/opt/python3.13-nogil/bin/python3 benchmark_test.py"


hyperfine -i --shell=none --output=pipe --runs 3 --warmup 2 -n "Python - GIL" "python benchmark_web_http_test.py"
hyperfine -i --shell=none --output=pipe --runs 3 --warmup 2 -n "Python - No GIL" "/opt/python3.13-nogil/bin/python3 benchmark_web_http_test.py"
