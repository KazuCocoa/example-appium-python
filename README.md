# example-appium-python

This repository is for Peaks.

## Environment

- Appium 1.15.0
- macOS 10.14.6 (18G84)
- Python 3.7.2
- node 10.16.0
- npm 6.9.0

## Install Appium environment

### Get npm environment

Install nodebrew since I like it

- https://github.com/hokaccha/nodebrew

```
nodebrew install-binary 10.16.0
nodebrew use 10.16.0
npm install -g appium@1.14.0
```

### clone this repository

install pypi

```
pip3 install -r 08/requirement.txt
```

### Launch appium

```
$ appium --relaxed-security
# [Appium] Welcome to Appium v1.14.0
# [Appium] Non-default server args:
# [Appium]   relaxedSecurityEnabled: true
# [Appium] Appium REST http interface listener started on 0.0.0.0:4723
```

**notice**
- 1.14.0 has no ability to run Appium against Xcode 11.
- Should wait for 1.15.0

### Run a simple test

```
$ python3 sample.py
.
----------------------------------------------------------------------
Ran 1 test in 12.177s

OK
```



