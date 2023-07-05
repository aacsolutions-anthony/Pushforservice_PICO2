# Instructions for configuring software on the PICO W for push service

![image](https://github.com/aacsolutions-anthony/Pushforservice_PICO2/assets/131961269/999eb655-1ae0-4f65-ac30-e258102ee683)

**AAC Solutions Anthony Grace** 

## Introduction:

This document provides detailed instructions on how to set up and program the Raspberry Pi Pico W using MicroPython, either on a Windows machine or a Linux machine. The guide walks you through the steps of downloading the necessary firmware, installing the Thonny IDE, configuring the interpreter, and writing and executing a Python script.

The guide also covers the steps for organizing your files on the Raspberry Pi Pico W, making sure they are in the correct locations and have the appropriate configurations for your WiFi network. Additional instructions are included for checking the results and ensuring your Python script runs correctly on the device.

Lastly, the document provides a set of instructions specifically for Linux users. These steps guide you through the process of installing the firmware, downloading your Python code, editing configuration files, and moving files to the Raspberry Pi Pico W using the Linux terminal.

## Scope:

This document is intended for users who are setting up a Raspberry Pi Pico W for the first time, as well as those looking to program the device using MicroPython. It provides separate instructions for Windows and Linux users, making it a comprehensive guide for individuals working on different operating systems.

The guide does not cover troubleshooting steps or the use of programming languages other than MicroPython. The reader is expected to have a basic understanding of how to use their operating system's terminal or command line interface. Moreover, this guide is tailored to a specific Python script which connects the Raspberry Pi Pico W to a WiFi network and performs a post request when a button is pressed. However, the principles and procedures can be applied to other projects as well.

---

### Initial Steps:
* Step 1: Setup the Raspberry Pi Pico W

Follow the following setup instructions. These include downloading the MicroPython firmware, setting up the Pico W in Device Firmware Update (DFU) mode, and transferring the firmware to the Pico W.
Install MicroPython onto Pico W

Follow these steps if it's your first time using a Pico W, or the Pico W does not have MicroPython currently installed.

* 1.1 Download MicroPython for Pico W - comes (with urequests and upip preinstalled)
* 1.2 Put your Pico W into Device Firmware Update mode as follows:
* 1.3 Hold the BOOTSEL button on the Pico W
* 1.4 Connect the Pico W to your computer via the USB cable
* 1.5 Release the BOOTSEL button

The Pico W will appear as a removable drive called RPI-RP2

* 1.6 Drag + Drop the MicroPython .uf2 file into RPI-RP2
* 1.7 Unplug your Pico W from USB, and plug it back in.

### Windows Install Method:

After the reboot, your Pico W is now running MicroPython

Step 2: Install Thonny

* If you haven't already installed Thonny, download it from the official website and follow the installation instructions there.

Step 3: Open Thonny and Configure Interpreter

* Open Thonny and go to "Run > Select Interpreter". From the interpreter options, choose "MicroPython (Raspberry Pi Pico)".

Step 4: Connect to your Pico W

* Navigate to "Run > Stop/Restart Backend" to connect to your Pico W.

Step 5: Create a New Script

* Go to "File > New" to create a new script. In the new blank script, copy the following Python code, or download the specified tarball from the aacsolutions GitHub.

* As of 5/7/23 this project calls for <pushbutton/pico2/*.py> etc - path may vary

Step 5.2 Organise the file structure of the PICO-w. Make sure that the python file, config.ini, and payload.json are all in the root directory of the PICO-w

* Be sure to replace 'your_wifi_ssid' and 'your_wifi_password' with your actual WiFi SSID and password in the config.ini

* Also make sure that the JSON payload suits your requirements and produciton environment (Deployment environment may be different to produciton)

Step 6: Save and Run the Script

* Go to "File > Save" to save your script. Then, go to "Run > Run current script" to run the script.
The program will connect your Raspberry Pi Pico W to your WiFi network and set it to make a post request to the specified URL with the specified JSON payload when the button is pressed.

Step 7: Check the Results

* Press the button connected to your Raspberry Pi Pico W. The output in Thonny's Shell pane should indicate whether the post request was successful or not.

### LINUX Install (Preffered)

Step 1: Install the Firmware

* Download the MicroPython firmware for Raspberry Pi Pico W from the official website. To do this via terminal, use wget:

```
wget https://micropython.org/resources/firmware/rp2-pico-2022-02-16-v1.18.uf2
```

Be sure to Replace the URL with the latest MicroPython firmware for the Raspberry Pi Pico W.
Connect the Pico W to your computer via USB and put it into DFU mode. Once connected, the Pico W will appear as a mass storage device named RPI-RP2.
Move the firmware file to the Pico W:

```
mv rp2-pico-2022-02-16-v1.18.uf2 /media/your_username/RPI-RP2
```

Replace 'your_username' with your actual username. Or the path to the PICO
Ofcourse your system could be different so double check the path with lsblk

```
lsblk
```

Step 2: Download Your Python Code

* If the Python code is on a GitHub repository, you can download it directly to your Raspberry Pi using git clone:

Although this should be shared in the teams chat or over email in a compressed tarball.

```
tar -xvf PICOTARBALL.tar.gz
```
**OR**

```
git clone https://github.com/your_username/your_repository.git
```

Replace 'your_username' and 'your_repository' with the appropriate information. This will download your entire repository to the current directory.

Step 3: Edit Configuration File

* You need to edit the config file and the JSON payload to suit your production environment.

- NOTING:
    * 1. SSID
    * 2. PSK
    * 3. URL - IP AND PATH

```
vim config.ini
```

Step 4: Move Files to Pico W

* To move your Python script, configuration file, and JSON payload file to the root directory of the Pico W, use the mv or cp command:

```
mv python.py /media/your_username/RPI-RP2
mv config.ini /media/your_username/RPI-RP2
mv payload.json /media/your_username/RPI-RP2
```

***WARNING:***
If you are going to do this as root or sudo, be sure to check the owner and group / GID of the file and directory with ls -lh to verify it isnt locked and is executable by the microcontroller.

```
lh -lh /media/YOUR USERNAME/RPI-RP2
```

Step 5: Check the Files on Pico W

* Double check the files on the Pico W to ensure they've been correctly transferred:

```
ls /media/your_username/RPI-RP2
```

Now you're ready to run your program on the Raspberry Pi Pico W!

**Note:**
The terminal commands might vary slightly depending on your Linux distribution. The above commands are for a Debian-based system. Though they should work on Arch and others aswell.

Congratulations! You've just programmed and configured your Raspberry Pi Pico W, verify the files in the config.ini and the payload.json
