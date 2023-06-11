# solution
Open in Ghidra and select the language / compiler specification:

- Processor: AVR8
- Variant: atmega256
- Compiler: gcc

These infos can be obtained by first runnings `strings` on the binary and then checking the exact microprocessor
(ATmega32U4) that is on the PCB (DZ60RGB-ANSI V2). [The QMK firmware repo can be useful for
this](https://github.com/qmk/qmk_firmware/tree/master/keyboards/dztech/dz60rgb_ansi).

The binary is not stripped and we have a lot of helpful funtion names that make our lives easier. We can look for all
strings in the binary and filter by the word `"flag"` to find the string `"Initializing flag LED animation"`. From this
we now know that there must be a flag hidden in some kind of LED animation. Ghidra even finds the label `flag_leds`
which we need later on to decode the LEDs into a flag.

Unfortunately, Ghidra isn't able to find the instructions that contain the custom code directly. There's multiple ways
to find it:
- We can compile our own firmware (exact model is known) and then diff the binaries
- We can check where `xputs` is called on our debug string `"Initializing flag LED animation"`

I chose the second option here because it's a bit easier. We go to `xputs` and go through the references to it:
```
     code:001182 86 ef           ldi        R24,0xf6
     code:001183 92 e0           ldi        R25,0x2
     code:001184 0e 94 52 04     call       xputs                                            undefined xputs()
```
One reference looks like this. Ghidra isn't smart enough to figure out that this is essentially `xputs(0x2f6)`.
The string we found earlier was at `codebyte:002f6` so we found the code that initializes the LEDs to print the flag:

```c
if (rgb_effect_params._2_1_ != '\0') {
  if ((debug_config & 1) != 0) {
    xputs();
  }
  current = R1R0._1_1_;
  Y = (undefined *)0x0;
  do {
    rgb_matrix_set_color(Y,0,0,0);
    Y = (undefined *)((int)Y + 1);
  } while ((byte)Y != 0x3e || Y._1_1_ != (byte)(R1R0._1_1_ + ((byte)Y < 0x3e)));
}

X = CONCAT11(timer.9._3_1_,timer.9._2_1_);
if (timer.9._3_1_ < g_rgb_timer._3_1_ ||
    (byte)(timer.9._3_1_ - g_rgb_timer._3_1_) <
    (timer.9._2_1_ < g_rgb_timer._2_1_ ||
    (byte)(timer.9._2_1_ - g_rgb_timer._2_1_) <
    (timer.9._1_1_ < g_rgb_timer._1_1_ ||
    (byte)(timer.9._1_1_ - g_rgb_timer._1_1_) < ((byte)timer.9 < (byte)g_rgb_timer)))) {
  Z = (byte *)CONCAT11(-((current < 0xea) + -3),current + 0x16);
  R25R24._0_1_ = *Z;
  rgb_matrix_set_color((byte)R25R24,0,0,0);
  R25R24 = (uint)current;
  R25R24 = R25R24 + 1;
  R25R24 = L0(R25R24,0x18);
  uVar4 = R25R24;
  bVar2 = (byte)R25R24;
  current = (byte)R25R24;
  R25R24 = R25R24 & 0xff00 | (uint)rgb_matrix_config._3_1_;
  hsv_to_rgb(R25R24,rgb_matrix_config._1_1_);
  uVar3 = (byte)R25R24;
  Y = (undefined *)CONCAT11((char)(uVar4 >> 8) - ((bVar2 < 0xea) + -3),bVar2 + 0x16);
  R25R24._0_1_ = *Y;
  rgb_matrix_set_color((byte)R25R24,R23,R22,uVar3);
  R18 = rgb_matrix_config._4_1_ + 0x10;
  if (0xef < rgb_matrix_config._4_1_) {
    R18 = 0xff;
  }
  R25R24 = (uint)R18;
  R1R0 = R25R24 * 0x10;
  R1R0 = 0;
  L0(3000,R1R0._1_1_);
  timer.9._0_1_ = (byte)g_rgb_timer + R22;
  timer.9._1_1_ = g_rgb_timer._1_1_ + R23 + CARRY1((byte)g_rgb_timer,R22);
  bVar9 = CARRY1(g_rgb_timer._1_1_,R23) ||
          CARRY1(g_rgb_timer._1_1_ + R23,CARRY1((byte)g_rgb_timer,R22));
  timer.9._2_1_ = g_rgb_timer._2_1_ + R1R0._1_1_ + bVar9;
  timer.9._3_1_ =
       g_rgb_timer._3_1_ + R1R0._1_1_ +
       (CARRY1(g_rgb_timer._2_1_,R1R0._1_1_) || CARRY1(g_rgb_timer._2_1_ + R1R0._1_1_,bVar9));
  X = CONCAT11(timer.9._3_1_,timer.9._2_1_);
}
```

If we manually clean this up, we get:

```c
if (rgb_effect_params._2_1_) {
  if (debug) {
    xputs("Initializing flag LED animation");
  }
  current = 0;
  Y = 0;
  do {
    rgb_matrix_set_color(Y,0,0,0);
    Y = Y + 1;
  } while (Y < 0x3e);
}

if (timer < g_rgb_time) {
  rgb_matrix_set_color(flag_leds[current], 0, 0, 0);
  current = L0(current + 1, 0x18);
  RGB rgb = hsv_to_rgb(rgb_matrix_config._1_1_);
  rgb_matrix_set_color(flag_leds[current], rgb.r, rgb.g, rgb.b);
  timer + offset;
}
```

We can further simplify this by checking [the QMK source
code for the effect_params type](https://github.com/qmk/qmk_firmware/blob/4020674163fc80914059c4c9c3be5c0ae00bd150/quantum/rgb_matrix/rgb_matrix_types.h#L56-L60)
and the [rgb_matrix_config
type](https://github.com/qmk/qmk_firmware/blob/4020674163fc80914059c4c9c3be5c0ae00bd150/quantum/rgb_matrix/rgb_matrix_types.h#L85-L94):

```c
if (params->init) {
  if (debug) {
    xputs("Initializing flag LED animation");
  }
  current = 0;
  for (int Y = 0; Y < 62; Y++) {
    rgb_matrix_set_color(Y,0,0,0);
  }
}

if (timer < g_rgb_time) {
  rgb_matrix_set_color(flag_leds[current], 0, 0, 0);
  current = L0(current + 1, 0x18);
  RGB rgb = hsv_to_rgb(rgb_matrix_config.hsv);
  rgb_matrix_set_color(flag_leds[current], rgb.r, rgb.g, rgb.b);
  timer + offset;
}
```

The only missing part is the `L0` function at this point. The function seems to be a pointer to `udivmodhi4` which is
just [the modulo operation of gcc](https://github.com/gcc-mirror/gcc/blob/master/libgcc/udivmodhi4.c). With this we have
everthing we need. We can go to `flag_leds` and convert them 1 by 1 to characters.

```
    mem:0216 22              undefined122h                     [0]
    mem:0217 18              undefined118h                     [1]
    mem:0218 0b              undefined10Bh                     [2]
    mem:0219 03              undefined103h                     [3]
    mem:021a 0b              undefined10Bh                     [4]
    mem:021b 0a              undefined10Ah                     [5]
    mem:021c 10              undefined110h                     [6]
    mem:021d 1f              undefined11Fh                     [7]
    mem:021e 18              undefined118h                     [8]
    mem:021f 25              undefined125h                     [9]
    mem:0220 26              undefined126h                     [10]
    mem:0221 02              undefined102h                     [11]
    mem:0222 1f              undefined11Fh                     [12]
    mem:0223 13              undefined113h                     [13]
    mem:0224 23              undefined123h                     [14]
    mem:0225 22              undefined122h                     [15]
    mem:0226 16              undefined116h                     [16]
    mem:0227 02              undefined102h                     [17]
    mem:0228 16              undefined116h                     [18]
    mem:0229 22              undefined122h                     [19]
    mem:022a 18              undefined118h                     [20]
    mem:022b 02              undefined102h                     [21]
    mem:022c 19              undefined119h                     [22]
    mem:022d 27              undefined127h                     [23]
    mem:022e 15              undefined115h                     [24]
    mem:022f 0f              undefined10Fh                     [25]
```

Conversion can be done using:
 - [Keymap](https://github.com/qmk/qmk_firmware/blob/master/keyboards/dztech/dz60rgb_ansi/dz60rgb_ansi.c#L74-L78)  
      ```
      { 13, 12, 11,     10,      9,  8,      7,      6,      5,  4,  3,  2,      1,      0 },
      { 27, 26, 25,     24,     23, 22,     21,     20,     19, 18, 17, 16,     15,     14 },
      { 40, 39, 38,     37,     36, 35,     34,     33,     32, 31, 30, 29, NO_LED,     28 },
      { 52, 51, 50,     49,     48, 47,     46,     45,     44, 43, 42, 41, NO_LED, NO_LED },
      { 60, 59, 58, NO_LED, NO_LED, 57, NO_LED, NO_LED, NO_LED, 56, 55, 54, NO_LED,     53 }
      ```
 - [Keyboard Image(https://keycapsss.com/media/image/fe/ac/ff/dz60-rgb-ansi-v2-layout-1.png)
