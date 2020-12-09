const exec = require('child_process').exec

exec('ls -al',(err, stdout, stder)=>console.log(stdout))
