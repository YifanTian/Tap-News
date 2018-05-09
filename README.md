# Tap-News
A Real Time News Scraping and Recommendation System using React, Node.js, MongoDB, and TensorFlow.

Website: www.smartanteater.com
If you like this project. Please give it a star. If you have any interesting idea about further development, just let me know!


#!/bin/bash
fuser -k 3000/tcp
fuser -k 4040/tcp
fuser -k 5050/tcp

service redis_6379 start
service mongod start

pip install -r requirements.txt

cd ./web_server/client
npm install

# npm run build
npm run-script build <br/>
cd ../server <br/>
npm install <br/>
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
