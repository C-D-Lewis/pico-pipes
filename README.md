# midi-motors

Playing MIDI files on stepper motors.

## Setup

Install depenencies:

```shell
pip3 install --user pretty_midi
```

## Prepate a MIDI file

First, compile the MIDI into an importable Python table of note events:

```shell
python3 compile.py $midiPath $trackList
```

Where `$trackList` is a comma-separated list of MIDI instrument tracks to play.
A list will be shown when `compile.py` is run with the names and number of notes
to aid selection.

## Play the compiled file

> This example uses a bi-polar stepper motor connected to a Raspberry Pi Pico
> via a stepper motor driver (currently EasyDriver)

```shell
rshell
```

Copy the main and built files:

```shell
cp main.py /pyboard
cp build.py /pyboard
```