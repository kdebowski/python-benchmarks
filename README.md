#### How to build image

To build image you need to provide framework you want to test. There 2 expected values: directory and project names. Example of how to build docker image for testing Flask application:

`docker build -t fw:flask --build-arg directory=frameworks --build-arg project=flask .`

`docker build` - is standard command to build image

`-t fw:flask` - gives name fw:flask

`--build-arg directory=frameworks` - specifies main directory
  
`--build-arg project=flask` - specifies subdirectory, which is project name. 

#### How to run container

If you have already built image, you can run your container. To do so use command below:

`docker run -d -p 8080:8080 --name fw_flask fw:flask`

It will start detached container with name fw_flask exposed port 8080.

#### How to test with wrk

Download docker image with `wrk`:

`docker pull williamyeh/wrk`

Run image with options:

`docker run --rm williamyeh/wrk -c 100 -d 10 -t 4 http://192.168.99.100:8080/`

It will run requests against URL: 192.168.99.100:8080

### Various

#### How to remove \<none\> images:

``` docker rmi $(docker images -f "dangling=true" -q)```