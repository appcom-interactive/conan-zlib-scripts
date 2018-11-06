# Conan zlib script

This repository contains the conan receipe that is used to build the zlib packages at [rgpaul bintray](https://bintray.com/manromen/rgpaul).

For Infos about the zlib library please visit [zlib.net](https://zlib.net).
The library is licensed under the [zlib License](https://zlib.net/zlib_license.html).
This repository is licensed under the [MIT License](LICENSE).

## Android

Coming soon

### Requirements

* [CMake](https://cmake.org/)
* [Conan](https://conan.io/)
* [Android NDK r18b](https://developer.android.com/ndk/downloads/)

## Debian 9 (Stretch)

Coming soon

### Requirements

* [CMake](https://cmake.org/)
* [Conan](https://conan.io/)
* build-essential, make, curl, git, unzip and zip (`apt-get install build-essential cmake curl git unzip zip`)

## iOS

To create a package for iOS you can run the conan command like this:

`conan create . zlib/1.2.11@rgpaul/stable -s os=iOS -s os.version=12.1 -s arch=armv7 -s build_type=Release -o shared=False`

### Requirements

* [CMake](https://cmake.org/)
* [Conan](https://conan.io/)
* [Xcode](https://developer.apple.com/xcode/)

## macOS

To create a package for macOS you can run the conan command like this:

`conan create . zlib/1.2.11@rgpaul/stable -s os=Macos -s arch=x86_64 -s build_type=Release -o shared=False`

### Requirements

* [CMake](https://cmake.org/)
* [Conan](https://conan.io/)
* [Xcode](https://developer.apple.com/xcode/)

## Windows 10

To create a package for Windows 10 you can run the conan command like this:

`conan create . zlib/1.2.11@rgpaul/stable -s os=Windows -s compiler="Visual Studio" -s compiler.runtime=MT -s arch=x86 -s build_type=Release -o shared=False`

### Requirements

* [CMake](https://cmake.org/)
* [Conan](https://conan.io/)
* [Visual Studio 2017](https://visualstudio.microsoft.com/de/downloads/)
