# Web App en Kubernetes

Este proyecto es una aplicación web simple que se despliega en Kubernetes. La arquitectura consiste en un front-end, un back-end y una base de datos, cada uno corriendo en su propio pod.


## Tecnologías Usadas

- **Front-end**: HTML servido a través de Nginx
- **Back-end**: Python
- **Base de datos**: PostgreSQL
- **Orquestación**: Kubernetes

## Requisitos Previos

- Docker
- Kubernetes (minikube, etc.)
- kubectl

## Instalación y Despliegue
 - upload-docker.sh -> sube las imágenes a DockerHub y construye los contenedores, no es necesario ejecutarlo si ya están las imágenes subidas a DockerHub
 - deploy-deployments.sh -> coge las imágenes de docker y despliega el cluster
 - run-services.sh -> ejecuta los servicios para exponer las ip fuera del cluster


