function getCharacterFreq(users){
const userMap = {};

for(user of users){
userMap[user] = (userMap[user] || 1) + 1;
}
return userMap;
}
