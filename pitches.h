#define PITCH_TABLE_SIZE 128

static const float pitch_table[128] = {
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,          // Ignored to here
  27.5,       // 21 >  A0
  29.14,      // 22 >  A#0/Bb0
  30.87,      // 23 >  B0
  32.7,       // 24 >  C1
  34.65,      // 25 >  C#1/Db1
  36.71,      // 26 >  D1
  38.89,      // 27 >  D#1/Eb1
  41.2,       // 28 >  E1
  43.65,      // 29 >  F1
  46.25,      // 30 >  F#1/Gb1
  49,         // 31 >  G1
  51.91,      // 32 >  G#1/Ab1
  55,         // 33 >  A1
  58.27,      // 34 >  A#1/Bb1
  61.74,      // 35 >  B1
  65.41,      // 36 >  C2
  69.3,       // 37 >  C#2/Db2
  73.42,      // 38 >  D2
  77.78,      // 39 >  D#2/Eb2
  82.41,      // 40 >  E2
  87.31,      // 41 >  F2
  92.5,       // 42 >  F#2/Gb2
  98,         // 43 >  G2
  103.83,     // 44 >  G#2/Ab2
  110,        // 45 >  A2
  116.54,     // 46 >  A#2/Bb2
  123.47,     // 47 >  B2
  130.81,     // 48 >  C3
  138.59,     // 49 >  C#3/Db3
  293.66,     // 50 >  D3      << Resonant, octave up (was 146.83)
  311.13,     // 51 >  D#3/Eb3 << Resonant, octave up (was 155.56)
  329.63,     // 52 >  E3      << Resonant, octave up (was 164.81)
  349.23,     // 53 >  F3      << Resonant, octave up (was 174.61)
  369.99,     // 54 >  F#3/Gb3 << Resonant, octave up (was 185)
  196,        // 55 >  G3
  207.65,     // 56 >  G#3/Ab3
  220,        // 57 >  A3
  233.08,     // 58 >  A#3/Bb3
  246.94,     // 59 >  B3
  261.63,     // 60 >  C4 (middle C)
  277.18,     // 61 >  C#4/Db4
  293.66,     // 62 >  D4
  311.13,     // 63 >  D#4/Eb4
  329.63,     // 64 >  E4
  349.23,     // 65 >  F4
  369.99,     // 66 >  F#4/Gb4
  392,        // 67 >  G4
  415.3,      // 68 >  G#4/Ab4
  440,        // 69 >  A4 concert pitch
  466.16,     // 70 >  A#4/Bb4
  493.88,     // 71 >  B4
  523.25,     // 72 >  C5
  554.37,     // 73 >  C#5/Db5
  587.33,     // 74 >  D5
  622.25,     // 75 >  D#5/Eb5
  659.26,     // 76 >  E5
  698.46,     // 77 >  F5
  739.99,     // 78 >  F#5/Gb5
  783.99,     // 79 >  G5
  830.61,     // 80 >  G#5/Ab5
  880,        // 81 >  A5
  932.33,     // 82 >  A#5/Bb5
  987.77,     // 83 >  B5
  1046.5,     // 84 >  C6
  1108.73,    // 85 >  C#6/Db6
  1174.66,    // 86 >  D6
  1244.51,    // 87 >  D#6/Eb6
  1318.51,    // 88 >  E6
  1396.91,    // 89 >  F6
  1479.98,    // 90 >  F#6/Gb6
  1567.98,    // 91 >  G6
  1661.22,    // 92 >  G#6/Ab6
  1760,       // 93 >  A6
  1864.66,    // 94 >  A#6/Bb6
  1975.53,    // 95 >  B6
  2093,       // 96 >  C7
  2217.46,    // 97 >  C#7/Db7
  2349.32,    // 98 >  D7
  2489.02,    // 99 >  D#7/Eb7
  2637.02,    // 100 > E7
  2793.83,    // 101 > F7
  2959.96,    // 102 > F#7/Gb7
  3135.96,    // 103 > G7
  3322.44,    // 104 > G#7/Ab7
  3520,       // 105 > A7
  3729.31,    // 106 > A#7/Bb7
  3951.07,    // 107 > B7
  4186.01,    // 108 > C8
  4434.92,    // 109 > C#8/Db8
  4698.64,    // 110 > D8
  4978.03,    // 111 > D#8/Eb8
  5274.04,    // 112 > E8
  5587.65,    // 113 > F8
  5919.91,    // 114 > F#8/Gb8
  6271.93,    // 115 > G8
  6644.88,    // 116 > G#8/Ab8
  7040,       // 117 > A8
  7458.62,    // 118 > A#8/Bb8
  7902.13,    // 119 > B8
  8372.02,    // 120 > C9
  8869.84,    // 121 > C#9/Db9
  9397.27,    // 122 > D9
  9956.06,    // 123 > D#9/Eb9
  10548.08,   // 124 > E9
  11175.3,    // 125 > F9
  11839.82,   // 126 > F#9/Gb9
  12543.85,   // 127 > G9
};
