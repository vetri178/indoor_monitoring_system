mv1 = 0.0
density1 = 0.0 
max_1 = 0.0 
lux1 = 0.0 
temp1 = 0.0
hum1 = 0.0
#<meta http-equiv="refresh" content="60">
def web_page():

        html = '''<!DOCTYPE html>
<html>
  <head>
    <title> SENSOR LAB </title>
   <meta http-equiv="refresh" content="5">
  </head>
  <body style="background-color:rgba(249,245,235);">
    <style>
      figure {
        border: 2px #830000 solid;
        margin: 10px;
      }

      figcaption {
        background-color: #830000;
        color: #ffffff;
        font-family: Linux sans;
        padding: 5px;
        text-align: center;
        font-size: 130%;
      }

      div {
        background-color: rgba(0, 162, 0, 0.2);
        color: rgba(0, 80, 255, 0.8);
        padding: 50px;
        box-shadow: 10px 10px 5px #aaaaaa;
        width: 250px;
        height: 250px;
        font-family: verdana;
        margin: 80px;
      }

      div img {
        width: 100px;
        height: 100px;
        position: relative;
        top: -30%;
        right: -30%;
      }

      h2 {
        position: relative;
        top: -25%;
      }

      h4 {
        position: relative;
        top: -50%;
      }
      span {
        color: black;
      }
    </style>
    <figure>
      <img src="https://www.tce.edu/themes/gavias_edmix/logo.svg" style="left:width:80px; height:80px;">
      <figcaption>
        <b>SENSOR LABAROTORY</b>
      </figcaption>
    </figure>
    <div>
      <h2>
        <center>ILLUMINATION</center>
      </h2>
      <img src="https://images.vexels.com/media/users/3/153761/isolated/preview/6fab8faa95d14cbd987be6cd2fc8416e-light-bulb-colored-stroke-icon.png">
      <h3 style="color:red">
        <center>'''+str(lux1)+" LUX"+'''</center>
      </h3>
    </div>
    
    <div style= "position:relative;left:1000px;top:-428px;">
      <h2>
        <center>TEMPERATURE</center>
      </h2>
      <img src="https://www.freeiconspng.com/thumbs/temperature-icon-png/temperature-icon-png-18.png">
      <h3 style="color:red">
        <center>'''+str(temp1)+'''<span style="color:red">&#176;</span> C</center>
      </h3>
    </div>
    
     <div style="position:relative;top:-228px;">
      <h2>
        <center>HUMIDITY</center>
      </h2>
      <img src="https://cdn-icons-png.flaticon.com/512/4005/4005831.png">
      <h3 style="color:red">
        <center>'''+str(hum1)+''' %</center>
      </h3>
    </div>
    
    <div style= "position:relative;left:1000px;top:-658px">
      <h2>
        <center>DUST</center>
      </h2>
      <img src="https://images.vexels.com/media/users/3/207013/isolated/preview/848b6791e34adb3be38cc9e46d072533-dust-cleaning-brush-icon.png" style="width:120px;height:120px;top:-45%;right:-25%">
      <h4 style="color:red">'''+"<span>mv: </span>"+str(mv1)+'''</h4>
      <h4 style="color:red">'''+"<span>DENSITY: </span>"+str(density1)+" ug/m3"+'''</h4>
      <h4 style="color:red">'''+"<span>MAX: </span>"+str(max_1)+" ug/m3"+'''</h4>
    </div>
  </body>
</html>'''
        return html
