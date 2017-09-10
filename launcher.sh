#!/bin/bash
fuser -k 3000/tcp
fuser -k 4040/tcp
fuser -k 5050/tcp

service redis_6379 start
service mongod start

pip install -r requirements.txt

cd ./web_server/client
npm install
npm run build
cd ../server
npm install
nodemon ./bin/www &
cd ../../backend_server
python service.py &
cd ../news_recommendation_service
python recommendation_service.py &
python click_log_processor.py &

echo "=================================================="
read -p "PRESS [ANY KEY] TO TERMINATE PROCESSES." PRESSKEY

kill $(jobs -p)
fuser -k 3000/tcp
service redis_6379 stop
service mongod stop

# Please delete below comment.
# First, cd week8. Then input command: chmod +x launcher.sh
#After that, input command to run web app tap-news: sudo ./launcher.sh