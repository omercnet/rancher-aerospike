/*jslint node: true, esversion: 6 */

var telnet = require('telnet-client');
var request = require('request');
var minutes = 1 || process.env.TIP_INTERVAL;

function tipNode(host, nodes) {
  var connection = new telnet();
  var params = {
    host: host,
    port: 3003,
    timeout: 1500
  };

  connection.connect(params)
  .then((prompt) => {
    for (var i = 0, len = nodes.length; i < len; i++) {
      connection.exec("tip:host="+nodes[i]+";port=3002");
    }
  }, (error) => {
    console.log('error:', error);
  });
}

(function tipper() {
  request({json: true,url: "http://rancher-metadata/2016-07-29/self/service/primary_service_name"},
    (error, response, service) => {
      if (!error && response.statusCode == 200) {
        request({json: true, url: 'http://rancher-metadata/2016-07-29/services/'+service+'/containers'},
          (error, response, nodes) => {
          if (!error && response.statusCode == 200) {
            for (var i = 0, len = nodes.length; i < len; i++) {
              console.log("Tipping " + nodes[i].primary_ip + " about the other nodes");
              tipNode(nodes[i].primary_ip, nodes);
            }
          }
        });
      }
    }
  );
  console.log("waiting " + minutes + " minutes before tipping again..");
  setTimeout(tipper, minutes * 60 * 1000);
})();
