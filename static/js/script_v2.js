$(function () {

try {
  var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  var recognition = new SpeechRecognition();
}
catch(e) {
  console.error(e);
  $('.no-browser-support').show();
  $('.app').hide();

}


var noteTextarea = $('#note-textarea');
var instructions = $('#recording-instructions');
var notesList = $('ul#notes');
var morehelp = $('#morehelp');
var example = $('#example');
var help = $('.help');
//var data = eval('{{data}}');

var noteContent = '';
var finishFlag=false;
var helpFlag=true;
var RcdingFlag=false;
var counter=0;
var inst = setInterval(change, 1000);


$('.no-browser-support').hide();
$('#save-note-btn').hide();
$('#morehelp').hide();
$('#example').hide();
$('#moreExample').hide();
help.hide();
$('#go-next-btn').hide();
$('#detail1').hide();



//function getInt(vars)
//{
//    return vars;
//}

// Get all notes from previous sessions and display them.
var notes = getAllNotes();
renderNotes(notes);

//var dynamic_data = JSON.parse(data);


/*-----------------------------
      Voice Recognition
------------------------------*/

// If false, the recording will stop after a few seconds of silence.
// When true, the silence period is longer (about 15 seconds),
// allowing us to keep recording even when the user pauses.
recognition.continuous = true;

// This block is called every time the Speech APi captures a line.
recognition.onresult = function(event) {

  // event is a SpeechRecognitionEvent object.
  // It holds all the lines we have captured so far.
  // We only need the current one.
  var current = event.resultIndex;

  // Get a transcript of what was said.
  var transcript = event.results[current][0].transcript;

  // Add the current transcript to the contents of our Note.
  // There is a weird bug on mobile, where everything is repeated twice.
  // There is no official solution so far so we have to handle an edge case.
  var mobileRepeatBug = (current == 1 && transcript == event.results[0][0].transcript);

  if(!mobileRepeatBug) {
    noteContent += transcript;
    noteTextarea.val(noteContent);
  }
};

recognition.onstart = function() {
  instructions.text('Voice recognition activated. Try speaking into the microphone.');
}

recognition.onspeechend = function() {
//    if (noteContent.length && !finishFlag) {
//        finishFlag=true;
//        $('#save-note-btn').show();
////        instructions.text('You were quiet for a while so voice recognition turned itself off. We have got your answer, so you can go next.');
//   }
}

recognition.onerror = function(event) {
  if(event.error == 'no-speech') {
    instructions.text('No speech was detected. Try again.');
  };
}



/*-----------------------------
      App buttons and input
------------------------------*/

//$('#start-record-btn').on('click', function(e) {
//  noteTextarea.val('');
//  noteContent = '';
//  recognition.start();
//  finishFlag=false;
//  $('#save-note-btn').hide();
//});
//
//
//$('#pause-record-btn').on('click', function(e) {
//  recognition.stop();
//  if(!noteContent.length) {
//        instructions.text('We could not hear from you. Please try again.');
//     }
//                          else{
//                            instructions.text('Cong! You can go next.');
//                            finishFlag=true;
//                            $('#save-note-btn').show();
//                            //show “go next”
//                          }
//});

$('#speak').on('click',function(e){
     if (!RcdingFlag)//start recording
        {
               noteTextarea.val('');
               noteContent = '';
               recognition.start();
               finishFlag=false;
               $('#save-note-btn').hide();
               $('#go-next-btn').hide();
               RcdingFlag=true;
               $("#speak").html('Stop');

               //startRecording();
               startRecordingMp3();
        }
    else //stop recording
        {
               recognition.stop();
               if(!noteContent.length) {
                instructions.text('We could not hear from you. Please try again.');
               }
               else{
                instructions.text('Cong! You can go next.');
                finishFlag=true;
                $('#save-note-btn').show();
                $('#go-next-btn').show();
               }
               RcdingFlag=false;
               $(this).html('Speak Again');

               //stopRecording();
               stopRecordingMp3();

               // Save note to localStorage.
               // The key is the dateTime with seconds, the value is the content of the note.
               saveNote(new Date().toLocaleString(), noteContent);

               // Reset variables and update UI.
               noteContent = '';
               renderNotes(getAllNotes());
               noteTextarea.val('');
               finishFlag=false;


        }
});


// Sync the text inside the text area with the noteContent variable.
//noteTextarea.on('input', function() {
//  noteContent = $(this).val();
//})

//$('#help-btn').on('click',function(e){
//                  help.toggle();
//                  });

$('#save-note-btn').on('click', function(e) {
  recognition.stop();

  if(!noteContent.length && !finishFlag) {
    instructions.text('Only after you answer this question, you can go next. If you have spoken, press stop button to finish.');
  }
  else {

    //go to the next page
                       //window.location.href='/jsint';

  }

});




example.on('click',function(e){
           $('#moreExample').show();
           example.hide();
           morehelp.hide();
           });

function change(){ //show up after 5 seconds
    counter++;
    if (counter>1) help.show();
    if (counter>5){
        morehelp.show();
        example.show();
        clearInterval(inst);
    }
}

$('#help-btn').mouseover(function(){
                         $('#detail1').show();
                         });
$('#help-btn').mouseout(function(){
                        $('#detail1').hide();
                        });

//notesList.on('click', function(e) {
//  e.preventDefault();
//  var target = $(e.target);
//
//  // Listen to the selected note.
//  if(target.hasClass('listen-note')) {
//    var content = target.closest('.note').find('.content').text();
//    readOutLoud(content);
//  }
//
//  // Delete note.
//  if(target.hasClass('delete-note')) {
//    var dateTime = target.siblings('.date').text();
//    deleteNote(dateTime);
//    target.closest('.note').remove();
//  }
//});



/*-----------------------------
      Speech Synthesis
------------------------------*/

//function readOutLoud(message) {
//    var speech = new SpeechSynthesisUtterance();
//
//  // Set the text and voice attributes.
//    speech.text = message;
//    speech.volume = 1;
//    speech.rate = 1;
//    speech.pitch = 1;
//
//    window.speechSynthesis.speak(speech);
//}



/*-----------------------------
      Helper Functions
------------------------------*/

//accept notes array and show them on the webpage
function renderNotes(notes) {
  var html = '';
  if(notes.length) {
    notes.forEach(function(note) {
      html+= `<li class="note">
        <p class="header">
          <span class="date">${note.date}</span>

        </p>
        <p class="content">${note.content}</p>
      </li>`;
    });
  }
  else {
    html = '<li><p class="content">You don\'t have any answers yet.</p></li>';
  }
  notesList.html(html);
}


function saveNote(dateTime, content) {
  localStorage.setItem('note-' + dateTime, content);
    // send to flask server
    // send post request
}


//Get notes from localStorage, return them as an array
function getAllNotes() {
  var notes = [];
  var key;
  for (var i = 0; i < localStorage.length; i++) {
    key = localStorage.key(i);

    if(key.substring(0,5) == 'note-') {
      notes.push({
        date: key.replace('note-',''),
        content: localStorage.getItem(localStorage.key(i))
      });
    }
  }
  return notes;
}


//function deleteNote(dateTime) {
//  localStorage.removeItem('note-' + dateTime);
//}

  });
