# Tap-News
A News Scraping and Recommendation System using React, Node.js, MongoDB, and TensorFlow.

If you like this project. Please give it a star. If you have any interesting idea about further development, just let me know!

# Run the job: 
#!/bin/bash <br/>
fuser -k 3000/tcp <br/>
fuser -k 4040/tcp <br/>
fuser -k 5050/tcp <br/>

service redis_6379 start <br/>
service mongod start <br/>

pip install -r requirements.txt <br/>

cd ./web_server/client <br/>
npm install <br/>

npm run build <br/>
npm run-script build <br/>
cd ../server <br/>
npm install <br/>
nodemon ./bin/www &  <br/>
cd ../../backend_server <br/>
python service.py & <br/>
cd ../news_recommendation_service <br/>
python recommendation_service.py & <br/>
python click_log_processor.py & <br/>

# Stop the jobs: 
fuser -k 3000/tcp <br/>
service redis_6379 stop <br/>
service mongod stop <br/>
