import tkinter as tk
import Adafruit_PCA9685
import time 
import math
import smbus

class Servo:
    def __init__(self):
        self.pwm_40 = Adafruit_PCA9685.PCA9685(0x40)
        self.pwm_41 = Adafruit_PCA9685.PCA9685(0x41) 
        # Set the cycle frequency of PWM  
        self.pwm_40.set_pwm_freq(50) 
        time.sleep(0.01) 
        self.pwm_41.set_pwm_freq(50) 
        time.sleep(0.01)             

    #Convert the input angle to the value of pca9685
    def setServoAngle(self,channel, angle):  
        if channel < 16:
            date = 4096 * ((angle * 10) + 850) / 20000
            self.pwm_41.set_pwm(channel, 0, int(date))
        elif channel >= 16 and channel < 32:
            channel-=16
            date = 4096 * ((angle * 10) + 850) / 20000
            self.pwm_40.set_pwm(channel, 0, int(date))
        #time.sleep(0.0001)
    def relax(self):
        for i in range(8):
            self.pwm_41.set_pwm(i+8, 4096, 4096)
            self.pwm_40.set_pwm(i, 4096, 4096)
            self.pwm_40.set_pwm(i+8, 4096, 4096)
def reset_robot():
    S.setServoAngle(13,0)
    slider_PF.set(0)
    S.setServoAngle(10,0)
    slider_PM.set(0)
    S.setServoAngle(31,0)
    slider_PR.set(0)
    S.setServoAngle(18,180)
    slider_SF.set(180)
    S.setServoAngle(21,180)
    slider_SM.set(180)
    S.setServoAngle(27,180)
    slider_SR.set(180)
def move_PF(angle):
    S.setServoAngle(13,angle)
    print("Move PF to " + str(angle))
def move_PM(angle):
    S.setServoAngle(10,angle))
    print("Move PM to " + str(angle))
def move_PR(angle):
    S.setServoAngle(31,angle))
    print("Move PR to " + str(angle))
def move_SF(angle):
    S.setServoAngle(18,angle)
    print("Move SF to " + str(angle))
def move_SM(angle):
    S.setServoAngle(21,angle)
    print("Move SM to " + str(angle))
def move_SR(angle):
    S.setServoAngle(27,angle)
    print("Move SR to " + str(angle))

if __name__ == '__main__':
    #Draw User Interface
    window = tk.Tk()

    frame_PF = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
    frame_PM = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
    frame_PR = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
    frame_Reset = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
    frame_SF = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
    frame_SM = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
    frame_SR = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)

    frame_PF.grid(row=2, column=1, padx=5, pady=5)
    frame_PM.grid(row=3, column=1, padx=5, pady=5)
    frame_PR.grid(row=4, column=1, padx=5, pady=5)
    frame_Reset.grid(row=3, column=2, padx=5, pady=5)
    frame_SF.grid(row=2, column=3, padx=5, pady=5)
    frame_SM.grid(row=3, column=3, padx=5, pady=5)
    frame_SR.grid(row=4, column=3, padx=5, pady=5)

    slider_PF = tk.Scale(master=frame_PF,from_=0, to=180, command=move_PF)
    label_PF = tk.Label(master=frame_PF, text=f"PF")
    slider_PM = tk.Scale(master=frame_PM,from_=0, to=180, command=move_PM)
    label_PM = tk.Label(master=frame_PM, text=f"PM")
    slider_PR = tk.Scale(master=frame_PR,from_=0, to=180, command=move_PR)
    label_PR = tk.Label(master=frame_PR, text=f"PR")
    button_Reset = tk.Button(master=frame_Reset, text="Reset", command=reset_robot)
    slider_SF = tk.Scale(master=frame_SF,from_=0, to=180, command=move_SF)
    label_SF = tk.Label(master=frame_SF, text=f"SF")
    slider_SM = tk.Scale(master=frame_SM,from_=0, to=180, command=move_SM)
    label_SM = tk.Label(master=frame_SM, text=f"SM")
    slider_SR = tk.Scale(master=frame_SR,from_=0, to=180, command=move_SR)
    label_SR = tk.Label(master=frame_SR, text=f"SR")

    slider_PF.pack()
    label_PF.pack()
    slider_PM.pack()
    label_PM.pack()
    slider_PR.pack()
    label_PR.pack()
    button_Reset.pack()
    slider_SF.pack()
    label_SF.pack()
    slider_SM.pack()
    label_SM.pack()
    slider_SR.pack()
    label_SR.pack()

    window.mainloop()

    #Main part of program
    S=Servo()
