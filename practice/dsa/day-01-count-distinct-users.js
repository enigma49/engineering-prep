function countDistinctUsers(users){
 const userSet = new Set();
 for(let user of users){
    userSet.add(user);
 }
return userSet.size;
}
