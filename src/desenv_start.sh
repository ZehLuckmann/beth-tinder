sudo docker kill roger-desenv
sudo docker rm roger-desenv
sudo docker run -d -it --name roger-desenv -v `pwd`:/src roger_img
sudo docker exec -it roger-desenv bash
