kubectl delete deployment backend
kubectl delete deployment frontend
kubectl delete deployment db


kubectl apply -f db-deployment.yaml

kubectl apply -f backend-deployment.yaml

kubectl apply -f frontend-deployment.yaml
