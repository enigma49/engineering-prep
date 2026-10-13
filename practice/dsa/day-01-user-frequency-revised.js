function getCharacterFreq(users){
const userMap = {};
for(const user of users){
userMap[user] = (userMap[user] || 0) + 1;
}
return userMap;
}
