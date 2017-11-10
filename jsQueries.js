
function callPHP_Connect(userinput){
   $.ajax({
        url: "Socket.php",
        data: { action: userinput },
        datatype: "json",
        type: "POST",
        success: function(data) { clickJStoPHPResponse(data); }
   });
}
/* Originalfunktion
function callPHP_xxx(event){
   $.ajax({
        url: "Socket.php",
        data: {id: event.target.id,action: "close"},
        datatype: "json",
        type: "POST",
        success: function(data) { clickJStoPHPResponse(data); }
   });
}
*/

 
function clickJStoPHPResponse(data) {
   // Antwort des Server ggf. verarbeiten
   var response = $.parseJSON(data);
   alert("Mein Ergebnis bei AxxG-AJAX: " + response);
}
