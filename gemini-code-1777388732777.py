from gpiozero import LED, Button
from time import sleep

# Konfiguracja pinu (lokalnie nie potrzebujemy PiGPIOFactory)
led = LED(17)
przycisk = Button(2) # Podłącz przycisk do GPIO 2 i GND

print("Test lokalny uruchomiony. Naciśnij przycisk lub czekaj na miganie.")

try:
    while True:
        if przycisk.is_pressed:
            print("Przycisk wciśnięty - zapalam diodę!")
            led.on()
        else:
            led.blink(on_time=0.5, off_time=0.5, n=1)
            print("Miganie testowe...")
        
        sleep(1)

except KeyboardInterrupt:
    print("Test przerwany.")