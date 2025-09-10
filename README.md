# System resource-monitor for raspberry pi
I have used a Raspberry Pi Zero 2W and an ssd1306 OLED module for display.

---
##  Circuit Pin Diagram

Connect your OLED to the zero as follows:

| Raspberry Pi Zero 2W         | SSD1306 OLED       |
|------------------------------|--------------------|
| VBUS (Pin 2) or 3V3 (Pin 1)  | VCC                |
| GND (Pin 9) or Pin 6         | GND                |
| GPIO 2 (Pin 3)               | SDA (Data Line)    |
| GPIO 3 (Pin 5)               | SCL (Clock Line)   |

---
- Now enable the `I2C` connection by typing `raspi-config` then enable I2C from the `interfaces`.
- Before runnig the script make sure to install all necessary modules listed in the `requirements.txt` file. `pip install -r requirements.txt`.
- Now download and run the python script in the repository `python3 monitor.py`.

---

# My YouTube tutorial
[Tutorial Link](https://youtu.be/-3GgHCfQUcw?si=b1__bHEdNQz3Efx9)

---
## Snapshots

https://github.com/user-attachments/assets/fb71c1d5-946b-44db-97c0-cfc8a31eed9b

![image_run](https://github.com/user-attachments/assets/cc89dfea-1719-416e-a69b-8b4d822f6148)
