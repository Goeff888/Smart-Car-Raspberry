<!DOCTYPE html>
<html lang="de">
 <head>
  <meta charset="utf-8">
  
  <script type="text/javascript" src="http://code.jquery.com/jquery-1.7.1.min.js"></script>
  <script type="text/javascript" src="jsQueries.js"></script>
  <link rel="stylesheet" type="text/css" href="css/general.css">
  <title>Webroboter steuern</title>
 </head>
 <body>
 <?php session_start();
 $_SESSION['status_online'] = 0; ?>
<img src="pics/SmartCarLogo_450x104.jpg">
 <table>
  <tr><td></td><td></td></tr>

 </table>


 <li>nach rechts drehen</li>
 <li>nach links drehen</li>
 <li>nach oben drehen</li>
 <li>nach unten drehen</li>
 
 
<p>
<form name="robotaccess" action="">
<input type="button" value="Verbinden" name = "con" id ="connect" onclick = "callPHP_Connect(document.robotaccess.con.name)">
<input type="button" value="Trennen"   name = "clo" id ="connect" onclick = "callPHP_Connect(document.robotaccess.clo.name)"><br>
<input type="button" value="^" name = "for" id ="drive_vertical" onclick="callPHP_Connect(document.robotaccess.for.name);">
<input type="button" value="v" name = "bac" id ="drive_vertical" onclick="callPHP_Connect(document.robotaccess.bac.name);">
<img id="car_top" src="pics/TopView.jpg"><br>
<input type="button" value="<" name = "lef" id ="drive_horizontal" onclick="callPHP_Connect(document.robotaccess.lef.name);">
<input type="button" value="STOP" name = "stop" id ="drive_horizontal" onclick="callPHP_Connect(document.robotaccess.lef.name);">
<input type="button" value=">" name = "rig" id ="drive_horizontal" onclick="callPHP_Connect(document.robotaccess.rig.name);"><br>


<iframe src="http://192.168.0.106:8081" width="320" height="240" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
<br>

</p>
</form>
 <form id="form">
		<input type="input" id="iofield">
		<button type="submit">Send</button>
	</form>
	
	<hr>
	
	<div id="output"></div>

  </body>
</html>