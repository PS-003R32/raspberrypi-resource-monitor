from psutil import virtual_memory, cpu_percent, disk_usage
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, LCD_FONT
from gpiozero import CPUTemperature

serial=i2c(port=1, address=0x3C)
device=ssd1306(serial)
cpu_temp=CPUTemperature()

def main():
        while True:
                cpu_usage=cpu_percent(interval=1)
                mem=virtual_memory()
                disk=disk_usage('/')
                with canvas(device) as draw:
                        text(draw, (0,0), f"CPU: {cpu_usage:0.1f}%", fill="white", font=proportional(LCD_FONT))
                        text(draw,(0,17), f"CPU_temp: {float(cpu_temp.temperature): 0.1f}C", fill="white", font=proportional(LCD_FONT))
                        text(draw, (0,30), f"RAM: {mem.percent:0.1f}%", fill="white", font=proportional(LCD_FONT))
                        text(draw, (0,45), f"Disk: {disk.percent:0.1f}%", fill="white", font=proportional(LCD_FONT))
                time.sleep(0.1)
if __name__=="__main__":
        try:
                main()
        except KeyboardInterrupt:
                pass
