docker build -t lab1:v1 .

docker save lab1:v1 > my_image.tar

docker run lab1:v1

Ran the above commands successfully, completed model training on the wine dataset.

![Output Screenshot](output.png)