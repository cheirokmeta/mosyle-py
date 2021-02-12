# mosyle-py
### INTRODUCTION

This project provides examples for accessing [Mosyle](https://mosyle.com) account & device data with their API.

### USAGE

Make sure to set ```token``` in *device.py* to your Mosyle API token first.

```
python devices.py --command [command] --device [device UDID]
```

Currently supported ```--command``` arguments:

* shutdown
* restart
* info

#### OUTPUT EXAMPLES

```
python devices.py --command info --device ########-################ | grep -A3 "osversion"
     "osversion": "14.5",
     "date_info": "1613081246",
     "carrier": "Redacted ",
     "roaming_enabled": "1",
```

### LICENSE
This project is distributed under the [GNU General Public License v2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).

### ATTRIBUTION

MOSYLE is a trademark of Mosyle Corporation. This project is not affiliated with the Mosyle Corporation.
