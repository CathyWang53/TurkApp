
//on document ready
//$(function () {
  var recorder = new MP3Recorder({
                                 bitRate: 128
                                 }), timer;
  
  
function startRecordingMp3() {
                    recorder.start(function () {
                                   console.log("recordButton clicked");
                                   //start timer,
                                   var seconds = 0, updateTimer = function(){
                                   $('#timer').text(seconds < 10 ? '0' + seconds : seconds);
                                   };
                                   timer = setInterval(function () {
                                                       seconds++;
                                                       updateTimer();
                                                       }, 1000);
                                   updateTimer();
                                   
                    });
  }
  
  
function stopRecordingMp3(blob) {
                    console.log("stopButton clicked");
                   recorder.stop();
                    console.log("test1");
                   //get MP3
                   clearInterval(timer);
                    console.log("test2");
                   recorder.getMp3Blob(function (blob) {
                                       console.log("Getting Mp3");
                                       //var blobUrl = window.URL.createObjectURL(blob);
                                       blobToDataURL(blob, function(url){
                                                     $('ol.convertedList')
                                                     .append('<li><strong> recording_' +
                                                             (new Date()) +
                                                             '_.mp3</strong><br/>' +
                                                             '<audio controls src="' + url + '"></audio>' +
                                                             '</li>');
                                                     });
                                       console.log("Get Mp3");
                                       });
                   }
  
  function blobToDataURL(blob, callback) {
  var a = new FileReader();
  a.onload = function (e) {
  callback(e.target.result);
  }
  a.readAsDataURL(blob);
  }
  
//  });
