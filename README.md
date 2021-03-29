# midi-motors

Playing MIDI files on stepper motors via Raspberry Pi Pico. A Python script
using `pretty_midi` loads a MIDI file and generates a `notes.h` C header file
defining the notes as a table of floats.


## Setup

Install depenencies:

```shell
pip3 install --user pretty_midi
```


## Prepare a MIDI file

First, compile the MIDI into an importable Python table of note events:

```shell
python3 compile.py $midiPath $trackList
```

Where `$trackList` is a comma-separated list of MIDI instrument tracks to play.
A list will be shown when `compile.py` is run with the names and number of notes
to aid selection. For example:

```shell
python3 compile.py midi/still_alive.mid 0,1
```


## Prepare Raspberry Pi Pico C++ SDK

```shell
# From home directory
cd && mkdir pico

# Install pico SDK
git clone -b master https://github.com/raspberrypi/pico-sdk.git
cd pico-sdk/
git submodule update --init

# Add export PICO_SDK_PATH="$HOME/pico/pico-sdk"
nano ~/.bash_profile
source ~/.bash_profile

# Setup build tools
brew install cmake
brew tap ArmMbed/homebrew-formulae
brew install arm-none-eabi-gcc

# In this repo, configure for GCC
cd cpp
mkdir build
cd build
cmake ..
```


## Build the Pico firmware

The MIDI is compiled into a C header, `cpp/notes.h`.

```shell
cd cpp/build
make
```

Finally, copy to the Pico by connecting while 'BOOTSEL' is pressed:

```shell
cp PicoApp.uf2 /Volumes/RPI-RP2/
```

If connected and powered, the Pico will play the tracks chosen on the motors!
