# pico-base

Base project files for Raspberry Pi Pico on Mac OS.

## Setup

```shell
# From home directory
cd && mkdir pico

# Install pico SDK
git clone -b master https://github.com/raspberrypi/pico-sdk.git
cd pico-sdk/
git submodule update --init
nano ~/.bash_profile  # Add export PICO_SDK_PATH="$HOME/pico/pico-sdk"

# Setup build tools
brew install cmake
brew tap ArmMbed/homebrew-formulae
brew install arm-none-eabi-gcc

# In VS Code, add CMake Tools extension

# Configure for GCC arm none...
mkdir build
cd build
cmake ..

# Build
make