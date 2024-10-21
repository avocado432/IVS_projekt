## Brief
TBD Calculator is a team assignment for IVS23/24L

## Features

- Basic arithmetic operations
- Advanced operations (nth root, power and factorial)
- Keyboard support

Full usage of features is documented in `user_manual.pdf`

## Environment

Ubuntu 64bit
## Installation 
### Using a .deb package
1. Download the `tbd-calculator.deb` package from the [latest release]( https://github.com/terez01/IVS_projekt2/releases/latest)
2. Install the package: 
```
sudo apt install ./tbd-calculator.deb
```
If you wish to uninstall the program:
```
sudo apt remove tbd-calculator
```
### Manual installation from source
1. Clone the install branch of repository 
```
git clone -b install https://github.com/terez01/IVS_projekt2.git
```
2. Run make in the `/src/` directory
```
make
```
3. Generate executable
```
pip install pyinstaller
pyinstaller --onefile --name tbd-calculator window.py --add-data=resources:resources
```
4. Make program system-wide
```
mv dist/tbd-calculator /usr/bin
cd ../install/
cp tbd-calculator/deb/usr/share/applications/tbd-calculator.desktop /usr/share/applications
cp tbd-calculator/deb/usr/share/pixmaps/tbd-calculator.png /usr/share/pixmaps
```
If you want to uninstall:
```
rm /usr/bin/tbd-calculator
rm /usr/share/applications/tbd-calculator.desktop
rm /usr/share/pixmaps/tbd-calculator.png
```

## Authors

### Team name: TBD
Tereza Magerková 
[xmager00](mailto:xmager00@stud.fit.vutbr.cz) \
Tereza Lapčíková
[xlapci03](mailto:xlapci03@stud.fit.vutbr.cz) \
Tomáš Španka
[xspankt00](mailto:xspankt00@stud.fit.vutbr.cz)

## Licence
This project is licenced under **GNU GPL-3.0-or-later**