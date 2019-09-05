from flask import Flask,render_template,redirect, url_for, request
import csv,time

app = Flask(__name__)

class Gettime(object):
  def Get(self):
    seconds=time.time()
    seconds=time.localtime(seconds)
    return str(seconds.tm_hour)+":"+str(seconds.tm_min)+":"+str(seconds.tm_sec)

class Csv(object):
  def writecsv(self,tim,temp,humi,timee):
    with open("09052019.csv","a+", newline='') as data:
      write= csv.writer(data,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      write.writerow([tim,temp,humi,timee])
    return None


class Template(object):
  def __init__(self):
    self.timee = Gettime()
    self.Csv= Csv()
  def writedata(self,tim,temp,humi):
    a=self.Csv
    a.writecsv(tim,temp,humi,self.timee.Get())


@app.route('/')
def home():
  return render_template("index.html")

@app.route('/log', methods=['GET'])
def log():
  tim=request.args.get("time")
  temp=request.args.get("temp")
  humi=request.args.get("humi")
  
  a=Template()
  a.writedata(tim,temp,humi)
  
  return render_template("Log.html")

if __name__== '__main__':
    app.run(debug = True, host='0.0.0.0', port=8080)