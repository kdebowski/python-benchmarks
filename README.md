#### How to build image?

To build image you need to provide framework you want to test. There 2 expected values: directory and project names. Example of how to build docker image for testing Flask application:

`docker build -t fw:flask --build-arg directory=frameworks --build-arg project=flask .`

#### How to run container?

If you have already built image, you can run your container. To do so use command below:

`docker run -d -p 8080:8080 --name fw_flask fw:flask`

It will start detached container with name fw_flask exposed port 8080.

#### How to test with wrk?

Download docker image with `wrk`:

`docker pull williamyeh/wrk`

Run image with options:

`docker run --rm williamyeh/wrk -c 100 -d 10 -t 4 http://192.168.99.100:8080/`

It will run requests against URL: 192.168.99.100:8080

### Results

Provided values are results of tests conducted on my personal computer. You will probably have completely different results on your machine. 

#### Specification of machine

- CPU: Intel Core i5-4200U 1.6 GHz (up to 2.6 GHz)
- Memory: 8 GB DDR3
- Drive type: SSD
- Docker for Windows (with full Virtualbox image)

#### Testing conditions

All tests are executed using common settings:
- web server (Gunicorn) is running with 4 workers
- wrk uses 100 connections
- wrk tests for 10 seconds
- wrk uses 4 threads

#### Frameworks

- [Aiohttp (3.4.4)](https://docs.aiohttp.org/en/stable/)
- [Bottle (0.12.13)](https://bottlepy.org/docs/dev/)
- [Falcon (1.4.1)](https://falconframework.org/)
- [Flask (1.0.2)](http://flask.pocoo.org/)

#### Results

##### Test case 1 - Hello World

| Framework | Requests/sec |
| :---: | :---: |
| Aiohttp | 585 |
| Falcon | 288 |  
| Bottle | 264 |
| Flask | 226 |

### Various

#### How to remove \<none\> images:

``` docker rmi $(docker images -f "dangling=true" -q)```