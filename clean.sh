docker stop $(docker ps -q)
# docker rm $(docker ps -a -q)
# docker rmi $(docker images -f "dangling=true" -q)
docker system prune -f
docker volume prune -f
