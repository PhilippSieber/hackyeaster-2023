'use strict';

const express = require('express');
const path = require('path');
const url = require('url');
const pug = require('pug');
const nodeEval = require('node-eval');

// Constants
const PORT = 1337;
const HOST = '0.0.0.0';

// App
const app = express();
app.disable('x-powered-by');

app.get('/', function (req, res) {
  let passphrase = req.query.passphrase;
  let reqUrl = url.format(url.parse(req.url, true));
  if (!passphrase) {
    res.send(pug.renderFile('index.pug'));
  } else if ((reqUrl.match(/passphrase/g) || []).length > 1) {
    res.send(pug.renderFile('blocked.pug', { message: 'passphrase param found more than once' }));
  } else if (!(typeof passphrase === "string")) {
    res.send(pug.renderFile('blocked.pug', { message: 'passphrase param has invalid type' }));
  } else if (passphrase.length > 75) {
    res.send(pug.renderFile('blocked.pug', { message: 'passphrase too long' }));
  } else {
    let invalidChar = getInvalidChar(passphrase);
    if (invalidChar) {
      res.send(pug.renderFile('blocked.pug', { message: 'found invalid character: ' + invalidChar }));
    } else {
      try {
        // run eval in new context {} - otherwiese users would see each others variables
        let evald = nodeEval(req.query.passphrase, '', {});
        if (evald == 'coneʸisland') {
          res.send(pug.renderFile('flag.pug'));
        } else {
          res.send(pug.renderFile('nope.pug'));
        }
      } catch (e) {
        res.send(pug.renderFile('blocked.pug', { message: 'invalid expression' }));
      }
    }
  }
});
app.get('/styles.css', function (req, res) {
  res.sendFile('/styles.css', { root: path.join(__dirname) });
});
app.get('/title.png', function (req, res) {
  res.sendFile('/title.png', { root: path.join(__dirname) });
});

// functions
function getInvalidChar(str) {
  if (str.includes('$')) return '$';
  if (str.includes('_')) return '_';
  if (str.includes('/')) return '/';
  if (str.includes('\\')) return '\\';
  if (/[a-zA-Z]/.test(str)) return 'letter';
  return null;
}

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
