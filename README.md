#### How to test with wrk

Download docker image with `wrk`:

`docker pull williamyeh/wrk`

Run image with options:

`docker run --rm williamyeh/wrk -c 100 -d 10 -t 4 http://192.168.99.100:8080/`

It will run requests against URL: 192.168.99.100:8080