hyperfine -i --shell=none --output=pipe --runs 3 --warmup 2 -n "GIL - Basic Threads" "make gil_normal" -n "NO GIL - Basic Threads" "make no_gil_normal"

hyperfine -i --shell=none --output=pipe --runs 3 --warmup 2 -n "GIL - Run HTTP Requests" "make gil_http" -n "NO GIL - Run HTTP Requests" "make no_gil_http"
