# Microservice1 - Get zipcode from given name of city.
Steps:
pdffile:
[Microservice1.pdf](https://github.com/Jinping4038/Microservice1/files/10566495/Microservice1.pdf)

Method1 - Run python file 
![image](https://user-images.githubusercontent.com/122847154/216265532-ad76324e-f700-41b4-90f3-061a0b2510e7.png)


http://127.0.0.1:8000/zipcode?city=Sunnyvale&state=CA
![image](https://user-images.githubusercontent.com/122847154/216265552-56a30c1a-ff99-4601-897c-b3d0d7fdbc52.png)


Method2 use command as following steps:
Build image: docker build -t microservice1:1.0 . 
![image](https://user-images.githubusercontent.com/122847154/216265582-666f1958-1d22-41d5-97b7-47b2fba6d738.png)


Run container: docker run -d -p8000:8000 microservice1:1.0  
list all the container: docker ps -a  
![image](https://user-images.githubusercontent.com/122847154/216265611-33c4f64a-33f5-442f-ab48-aed2c407558b.png)


Check logs, see what happening inside the container:
docker logs f58f0f08395c  
![image](https://user-images.githubusercontent.com/122847154/216265636-e021a08f-0336-4d17-b41e-2cc59fb7ef43.png)


http://127.0.0.1:8000/zipcode?city=Sunnyvale&state=CA
![image](https://user-images.githubusercontent.com/122847154/216265653-87187de9-4a7b-49f9-b2d4-2fb057583760.png)

Microservice2 % docker build -t microservice1:1.0 .
![image](https://user-images.githubusercontent.com/122847154/216265688-290485c4-201c-40c2-9df9-b289e7fd4d79.png)

docker login
We need to tag the image, because docker doesn’t know which repository storing it.
docker tag microservice1:1.0 jinping4038/microservice1
Store the docker image in repository 
docker push jinping4038/microservice1
![image](https://user-images.githubusercontent.com/122847154/216265732-bf379fda-f8a6-4d11-97ae-6ac5eb020b85.png)

Download the docker image from the repository
docker pull jinping4038/microservice1
Run the docker image on port 8000.
docker run -d -p8000:8000 jinping4038/microservice1
![image](https://user-images.githubusercontent.com/122847154/216265776-9b8c43cc-4880-4108-a8d5-829b12a6c6c8.png)
![image](https://user-images.githubusercontent.com/122847154/216265790-9c4af891-4ee0-4c59-a775-e5efe30fb2ee.png)

Here is the link of the docker image in docker hub:
https://hub.docker.com/r/jinping4038/microservice1

![image](https://user-images.githubusercontent.com/122847154/216265820-05c237cc-5c9b-450b-bc99-4b6f47eb4729.png)




