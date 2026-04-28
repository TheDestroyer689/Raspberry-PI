# Aktualizacja repozytoriów
sudo apt update

# Instalacja pakietu pigpio
sudo apt install pigpio python3-pigpio -y

# Uruchomienie demona z flagą -l (nasłuchiwanie w sieci)
# Domyślnie pigpiod pozwala na połączenia zdalne, ale warto to wymusić:
sudo pigpiod