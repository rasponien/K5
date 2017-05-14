# K5
### 1. Installeerida mongoDB
------
### 2. Lisada mongoDB path environmental variable'desse 
##### (Windowsis - C:\Program Files\MongoDB\Server\3.4\bin)
------
### 3. Panna käsurealt mongodb server käima 
##### Kui path on ära määratud, siis minul on näiteks nii 
##### mongod --dbpath C:/Users/carlcustav/Veebiarhitektuur/K5/data	
##### siis salvestab andmed sinna kohta
------
### 4. Vaja võtta uus cmd aken ja connectida instance'ga 
##### mongo --port 27017
------
### 5. Viimasena lisatud aknas kasutada käsku - use WordPronunciationDB 
##### (vb vaja lisada ka user ja pwd (vaata createuser) - https://docs.mongodb.com/manual/tutorial/enable-authentication/)
------
### 6. Nüüd saab läbi shelli andmeid lisada ja ühendus andmebaasiga peaks olemas olema
##### a = Word()
##### a.word = "asdfasdf" jne jne
##### a.save()
