from flask import Flask, render_template, request
import datetime
import time
app=Flask(__name__)

@app.route('/')
def inicio():


  return render_template('index.html')

def escribir(tiempo,temp,hum):
  hora= time.localtime()
  horaT= time.strftime("%H:%M:%S", hora)
  print(horaT)
  datos=open("09052019.csv","a+")
  datos.write("\r\n"+horaT+", "+tiempo+", "+ temp+ ", "+ hum )
  datos.close()

@app.route('/log', methods=['GET'])
def guardar():

  tiempo = request.args.get('tiempo')
  temp = request.args.get('temperatura')
  hum = request.args.get('humedad')
  escribir(tiempo,temp,hum)
  return render_template('index.html')






app.run(debug=True)
