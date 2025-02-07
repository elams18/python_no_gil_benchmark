make gil_normal:
	python benchmark_test.py
make no_gil_normal:
	/opt/python3.13-nogil/bin/python3 benchmark_test.py
make gil_http:
	python benchmark_web_http_test.py
make no_gil_http:
	/opt/python3.13-nogil/bin/python3 benchmark_web_http_test.py
