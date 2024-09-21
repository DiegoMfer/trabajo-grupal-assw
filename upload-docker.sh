docker build -t frontend:latest ./frontend
docker build -t backend:latest ./backend

docker tag frontend:latest monsterultrafiesta/frontend:latest
docker tag backend:latest monsterultrafiesta/backend:latest

docker push monsterultrafiesta/frontend:latest
docker push monsterultrafiesta/backend:latest

# Eliminar las imágenes
docker rmi frontend:latest
docker rmi backend:latest
docker rmi monsterultrafiesta/frontend:latest
docker rmi monsterultrafiesta/backend:latest
