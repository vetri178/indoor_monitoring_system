import machine,time
from machine import Pin,I2C
from time import sleep
try:
    import usocket as socket
except:
    import socket
import bh17502
from bus_service import I2cAdapter
import network
import urequests
import esp,gc
import dht
from html import*

sensor = dht.DHT11(Pin(14))

esp.osdebug(None)
gc.collect()

api_key = 'dZCTb9jv_r6Koe2xmbxCbo'

LED_PIN = machine.Pin(16, machine.Pin.OUT)  # D0
VO_PIN = machine.ADC(0)  # A0

SAMPLING_TIME = 0.00028
DELTA_TIME = 0.00004
SLEEP_TIME = 0.00968
VOC = 0.6
MAX = 0

scl = machine.Pin(5)
sda = machine.Pin(4)
i2c = machine.I2C(scl,sda)
    
adaptor = I2cAdapter(i2c)
sol = bh17502.Bh1750(adaptor)

sol.power(on=True)     
sol.set_mode(continuously=True, high_resolution=True)
sol.measurement_accuracy = 1.0    
old_lux = curr_max = 1.0

def calc_volt(val):
    return val * 3.3 / 1024

def calc_density(vo, k=0.5):
    global VOC
    global MAX

    dv = vo - VOC
    if dv < 0:
        dv = 0
        VOC = vo
    density = dv / k * 100
    MAX = max(MAX, density)
    return density

def callback(density):
    if density == 0:
        seq = "0.0"
    else:
        seq = str(round(density, 1))

def monitor(sample_size=100, callback=None):
    vals = []
    while True:
        try:
            LED_PIN.value(0)
            sleep(SAMPLING_TIME)
            vals.append(VO_PIN.read())
            sleep(DELTA_TIME)
            LED_PIN.value(1)
            sleep(SLEEP_TIME)
            if len(vals) == sample_size:
                avg = sum(vals) / len(vals)
                volt = calc_volt(avg)
                mv = volt * 1000
                density = calc_density(volt)        
                vals = []
                
                if callback:
                    callback(density)
                    
                return mv,density,MAX
                #dust1 = str(mv)+str(density)+str(max_)
        except KeyboardInterrupt:
            break
        except Exception:
            raise
        finally:
            LED_PIN.value(0)
        
def light1():
     old_lux = curr_max = 1.0
     for lux in sol:
        if lux != old_lux:
            curr_max = max(lux, curr_max)
            return lux
       
        old_lux = lux        
        time.sleep_ms(sol.get_conversion_cycle_time())
        

def dht_11():
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    return temp,hum
    #temp_f = temp * (9/5) + 32.0
        

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(0)
s.settimeout(0.5)
s.bind(('', 80))
s.listen(5)


if __name__ == '__main__':
    
   while True:
  
        global mv1 
        global density1 
        global max_1
        global lux1

        mv1,density1,max_1 = monitor()
       
        #curr_max1 = light()
        lux1 = light1()
        #normalize1 = light2()
        temp1,hum1 = dht_11()
       
        try:        
            sensor_readings = {'value1':lux1 ,'value2':density1 ,'value3':max_1}
            print(sensor_readings)
            request_headers = {'Content-Type': 'application/json'}  
            request = urequests.post(
            'http://maker.ifttt.com/trigger/LIGHT_DUST/with/key/' + api_key,
            json=sensor_readings,
            headers=request_headers)
            #print(request.text)
            request.close()
            
            sensor_readings = {'value1':temp1 ,'value2': hum1 }
            print(sensor_readings)
            request_headers = {'Content-Type': 'application/json'}
            request = urequests.post(
            'http://maker.ifttt.com/trigger/TEMP_HUM/with/key/' + api_key,
            json=sensor_readings,
            headers=request_headers)
            #print(request.text)
            request.close()
           
            if gc.mem_free() < 102000:
              gc.collect()
            conn, addr = s.accept()
            conn.settimeout(3.0)
            print('Got a connection from %s' % str(addr))
            request = conn.recv(1024)
            conn.settimeout(None)
            request = str(request)
            print('Content = %s' % request)
            response = web_page()
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()
        except OSError as e:
            print('Connection closed')
            print('Failed to read/publish sensor readings.')
