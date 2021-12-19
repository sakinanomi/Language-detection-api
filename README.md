# Language-detection-api
This is for college mini project.
The project is a langugae detection project that will predict the languagee of the given input string

The trained ML model is taken from <link><br>
- The model is serialized and deserialized using pickle
- The API of the model is created using Flask
- Testing can be done using postman

#### Learnings
- Using Pickle
- Flask
- Postman

#### To use the API
This API takes a json with key value 'text', and returns a json with key 'predicted'

- Fork the repository
- Clone the repository using command git clone https://github.com/{your_username}/Language-detection-api.git
- Navigate to your directory
- open cmd and run the command api.py
- Now open postman and create an environment choose the post method in dropdown
- Enter the right URL (on which the api.py is running) with the correct port number in Postman
- Test in the body section sending the json for eg. {"text":"ถนนเจริญกรุง อักษรโรมัน thanon charoen krung เริ่มตั้งแต่ถนนสนามไชยถึงแม่น้ำเจ้าพระยาที่ถนนตก กรุงเทพมหานคร เป็นถนนรุ่นแรกที่ใช้เทคนิคการสร้างแบบตะวันตก ปัจจุบันผ่านพื้นที่เขตพระนคร เขตป้อมปราบศัตรูพ่าย เขตสัมพันธวงศ์ เขตบางรัก เขตสาทร และเขตบางคอแหลม"} <br>
or {"text": "klement gottwaldi surnukeha palsameeriti ning paigutati mausoleumi surnukeha oli aga liiga hilja ja oskamatult palsameeritud ning hakkas ilmutama lagunemise tundemärke  aastal viidi ta surnukeha mausoleumist ära ja kremeeriti zlíni linn kandis aastatel – nime gottwaldov ukrainas harkivi oblastis kandis zmiivi linn aastatel – nime gotvald"}
- Now send using the given button.
- The predicted language should be visible in the sections below



##### To work on

remove the hardcoded key value names

