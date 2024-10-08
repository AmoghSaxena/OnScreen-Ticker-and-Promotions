# **ARCHIVAL NOTICE**

**This repository is now being archived as a new version is in progress. The new version of this repository is available at [https://github.com/AmoghSaxena/ticker-v2](https://github.com/AmoghSaxena/ticker-v2)**

Please note that this repository will no longer be actively maintained or updated. All future development and updates will be made to the new version. We recommend using the new version for any new projects or contributions.

---

# OnScreen-Ticker-and-Promotions
A Linux Program for On-Screen Advertisements and promotions like shown in News Channels.

## Dependencies are mentioned below. ##

### OS related Dependency ###
1. Linux OS (recommended Ubuntu)
2. Desktop Environment Like `Ubuntu(Gnome/Mate/Lite/etc) - with hidden decorators and alwaysOnTop support`, `Fluxbox - with hidden decorators and alwaysOnTop support`
> If you want to disable the decorator in Gnome then check my Stack Overflow solution over here : [StackOverflow Link](https://stackoverflow.com/a/71908794/8813647)
3. Supported Python Version 3.6 [![Supported Python Version 3.6+](https://img.shields.io/badge/Python-v3.6+-blue.svg?style=flat-square&logo=python)](https://github.com/AmoghSaxena/OnScreen-Ticker-and-Promotions) BUT Recommended Python Version 3.8 [![Supported Python Version 3.6+](https://img.shields.io/badge/Python-v3.8+-blue.svg?style=flat-square&logo=python)](https://github.com/AmoghSaxena/OnScreen-Ticker-and-Promotions)

### Tools for Proper working of Ticker ###
* virtualenv 
* pkg-config 
* libcairo2-dev 
* python3-dev 
* gcc 
* libgirepository1.0-dev 
* python3-gi 
* gobject-introspection 
* gir1.2-gtk-3.0

For Ubuntu you can install them with following command:
```shell
sudo apt install -y virtualenv pkg-config libcairo2-dev python3-dev gcc libgirepository1.0-dev python3-gi gobject-introspection gir1.2-gtk-3.0
```
For Other distribution other than Ubuntu can install dependencies with similar commands found. You can refer Internet for same.

## Installation for stand-alone without services ##

### Procedure to Install this code ###
#### 1. Clone the Repo ####
```shell
$ git clone https://dvgit.digivalet.com/scm/dvcsof/tickerv2.git
```

#### 2. Change the working directory to cloned directory
```shell
$ cd ticker
```

#### 3. Run `Installation.sh` file ####
If `installation.sh` is already executable then you can directly run it with
```shell
 $ ./installation.sh
```
OR

If `installation.sh` is not executable then you can make it executable and run it with
```shell
$ chmod +x ./installation.sh
$ ./installation.sh
```
> This will create Virtual Environment in the parent directory & Install following pip modules which are required. 
> 
> > ![d](https://img.shields.io/badge/pip-latest-blue.svg?style=flat-square&logo=python)
> > ![d](https://img.shields.io/badge/pygame-2.1.0-blue.svg?style=flat-square&logo=python)
> > ![d](https://img.shields.io/badge/moviepy-1.0.3-blue.svg?style=flat-square&logo=python)
> > ![d](https://img.shields.io/badge/colorama-0.4.4-blue.svg?style=flat-square&logo=python)
> > ![d](https://img.shields.io/badge/PyGObject-3.42.0-blue.svg?style=flat-square&logo=python)

#### 4. Change `config.json` according to your needs
```json
{
   "static_ticker_condition": true,
   "position_static_ticker": "top-left",
   "static_ticker_bgcolor": [
      0,
      0,
      0
   ],
   "static_ticker_logo": true,
   "static_ticker_message": "Yeah!",
   "static_ticker_font_color": "#ffffff",
   "static_ticker_font_size": 40,
   "static_ticker_font": "Ubuntu",
   "main_ticker_condition": true,
   "main_ticker_message": "Multiple commands can be specified a the same time and there\u2019s also a delay that sleeps a certain amount of milliseconds before next command is executed. Here\u2019s an example where select is pressed, followed by left after waiting a second:",
   "main_ticker_logo": true,
   "main_ticker_logo_position": "left",
   "main_ticker_font": "MyriadProFont",
   "main_ticker_bgcolor": [
      255,
      0,
      0
   ],
   "main_ticker_font_color": [
      255,
      255,
      255
   ],
   "main_ticker_speed": "fast",
   "main_ticker_motion": "right-left",
   "optional_ticker_condition": true,
   "optional_ticker_message": "Multiple commands can be specified a the same time and there\u2019s also a delay that sleeps a certain amount of milliseconds before next command is executed. Here\u2019s an example where select is pressed, followed by left after waiting a second:",
   "optional_ticker_font": "MyriadProFont",
   "optional_ticker_bgcolor": [
      255,
      162,
      5
   ],
   "optional_ticker_font_color": [
      0,
      0,
      0
   ],
   "optional_ticker_speed": "fast",
   "optinal_ticker_motion": "left-right",
   "moving_ticker_condition": true,
   "moving_ticker_localtion": "center",
   "moving_ticker_center_size": "small",
   "time_interval": 197
}
```

#### 5. Run the program with ```start_ticker``` file ####
If `start_ticker` is already executable then you can directly run it with
```shell
 $ ./start_ticker
```
OR

If `start_ticker` is already executable then you can directly run it with
```shell
$ chmod +x .start_ticker
$ ./start_ticker
```
> This will create start the ticker and will run till the `"time_interval"` seconds in `config.json`
>
> Example: 
> > "time_interval": 197

> If In Emergency you need to stop the ticker then you can run `stop_ticker`
> 
> If `stop_ticker` is already executable then you can directly run it with
> ```shell
> $ ./stop_ticker_force
> ```
> OR
> 
> If `stop_ticker` is already executable then you can directly run it with
> ```shell
> $ chmod +x ./stop_ticker_force
> $ ./stop_ticker_force
> ```


### Changlogs
```
Changes between 1.2 and 1.3:
--------------------------------

Core:
 * Fixed Font length issue for English Language.
 * Fixed Free Font issue for languages
 * Changed `mid` to `normal` in font-size. Same as dashboard to fix previous ticker runnning issue.
 * Fixed API Issue for launching previous ticker


Changes between 1.1 and 1.2:
--------------------------------

Core:
 * Added Closing API Support
 * Fixed Font length issue for English Language.
 * Fixed Priority and API get-config Issue.
 * Fixed & Implemented DND support for ticker.


Changes between 1.0 and 1.1:
--------------------------------

Platform support changes:
 * Python 3.8:
     - Python 3.8 Now automatically installs with the Artifact
     - No need to install pip modules in virtual environment

Core:
 * Added Free Font style
     - Single font will be used for multiple languages
 * Optimized the code for the memory usage and thread-counts
 * Added Bash script which will now start and stop ticker using Ticker Services.


Changes for 1.0:
--------------------------------

Core:
 * Added Ticker and Its Enhancements including Python 3.6 Support
```
