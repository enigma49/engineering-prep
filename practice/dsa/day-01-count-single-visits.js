function getDistinctCharCount(userIds){
const userIdMap = {};
for(let userId of userIds){
 userIdMap[userId] = (userIdMap[userId] || 0) + 1;
}
let count = 0;
for(let user of Object.entries(userIdMap)){
 if(user[1] === 1) count++;
}

return count;

}
