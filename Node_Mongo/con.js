const mongoose = require('mongoose')

mongoose.connect('mongodb://127.0.0.1:27017/test')
const db = mongoose.connection
db.on('error', console.error) // mongoDB 연동 실패 시 에러 메시지 출력
db.once('open', () => {
  console.log('connected to mongoDB server') // mongoDB 연동 성공 시 메시지 출력
})

var userSchema = mongoose.Schema({
  name: 'string',
  age: 'number',
  sex: 'string',
  height: 'number'
})

// compiels our schema into a model
var test = mongoose.model('test', userSchema)
/*
// add user1 and user2 to "User" model
var user1 = new test({ name: 'Sohee', age: 24, sex: 'female', height: 162 })
var user2 = new test({
  name: 'Haelee',
  age: 28,
  sex: 'female',
  height: 170
})

// save user1
user1.save(function (err, data) {
  if (err) {
    // TODO handle the error
    console.log('error')
  } else {
    console.log('Saved!')
  }
})

// save user2
user2.save(function (err, data) {
  if (err) {
    // TODO handle the error
    console.log('error')
  } else {
    console.log('Saved!')
  }
})
*/
test.find(function (error, test) {
  console.log('------Read all-------')
  if (error) {
    console.log(error)
  } else {
    console.log(test)
  }
})
