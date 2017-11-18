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
<div align="center"><img src="pics/SmartCarLogo_450x104.jpg"></div> 
 
<p>
<form name="robotaccess" action="">
<div align = "center">
 <input type="button" value="Verbinden" name = "con" id ="connect" onclick = "callPHP_Connect(document.robotaccess.con.name)">
 <input type="button" value="Trennen"   name = "clo" id ="connect" onclick = "callPHP_Connect(document.robotaccess.clo.name)">
</div>

<table>
 <tr>
  <td colspan="4" id="control_header"></td>
 </tr>
 <tr>
  <td><input type="button" value="^" name = "for" id ="vertical_active" onclick="callPHP_Connect(document.robotaccess.for.name);"></td>
  <td rowspan = "2"><img width = "320" height="240" "id="car_top" src="pics/BerryCar.jpg"></td>
  <td rowspan = "2"><img width = "320" height="240" "id="no_cam" src="pics/camera_icon320x240.jpg"></td>
  <!-- 
  <td rowspan = "2"><iframe src="http://192.168.0.107:8081" width="320" height="240" frameborder="0" allowfullscreen="allowfullscreen"></iframe></td>
  -->
  <td><input type="button" value="^" name = "cup" id ="vertical_active" onclick="callPHP_Connect(document.robotaccess.cup.name);"></td>
 </tr>
 <tr>
  <td><input type="button" value="v" name = "bac" id ="vertical_active" onclick="callPHP_Connect(document.robotaccess.bac.name);"></td>
  <td><input type="button" value="v" name = "cdo" id ="vertical_active" onclick="callPHP_Connect(document.robotaccess.cdo.name);"></td>
 </tr>
<tr><td></td>
 <td>
  <input type="button" value="<" name = "lef" id ="small_horiz_active" onclick="callPHP_Connect(document.robotaccess.lef.name);">
  <input type="button" value="&#10006;" name = "stop" id ="small_horiz_active" onclick="callPHP_Connect(document.robotaccess.lef.name);">
  <input type="button" value=">" name = "rig" id ="small_horiz_active" onclick="callPHP_Connect(document.robotaccess.rig.name);">
 </td>
 <td>
   <input type="button" value="<" name = "cle" id ="big_horiz_active" onclick="callPHP_Connect(document.robotaccess.lef.name);">
   <input type="button" value=">" name = "cri" id ="big_horiz_active" onclick="callPHP_Connect(document.robotaccess.rig.name);">
 </td>
</tr>
</table>

</form>
 <form id="form">
		<input type="input" id="iofield">
		<button type="submit">Send</button>
	</form>
	

  </body>
</html>