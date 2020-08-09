const express = require('express');
const app = express();
app.listen(3000, () => console.log('listening at 3000'));
app.use(express.static('public'));
app.use(express.json({limit: '1mb'}));

var V1, R1, R2, simRez;
var exec = require('child_process').exec;
var readline = require('readline');
var fs = require('fs');

function get_line(filename, line_no, callback) {
  var data = fs.readFileSync(filename, 'utf8');
  var lines = data.split("\n");

  callback(null, lines[+line_no]);
}

function writeData(){
  const fs = require('fs');
  fs.writeFileSync('./voltageDiv.net', "Voltage divider netlist\nV1 1 0 "+V1+"\nR1 2 1 "+R1+"\nR2 0 2 "+R2+"\n.control\nop\nprint allv\n.endc\n.end");
}

app.post('/voltsim', (request, response) => {
  console.log(request.body);
  const data1 = request.body;
  V1 = data1.valV1;
  R1 = data1.valR1;
  R2 = data1.valR2;
  writeData();
  exec('ngspice voltageDiv.net -b -o dividerLog');
  setTimeout(() => {
    get_line('./dividerLog', 9, function(err, line){
      try {
        simRez = line.replace('v(2) = ','');
      }
      catch(err) {
        console.log(err.message);
      }
      console.log(simRez);
    });
    response.json({
      status: 'success',
      rezultats: simRez
    });
  }, 100);
});
