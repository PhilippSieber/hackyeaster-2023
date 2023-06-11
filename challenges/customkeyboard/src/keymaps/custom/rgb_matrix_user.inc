RGB_MATRIX_EFFECT(flag_led)

#ifdef RGB_MATRIX_CUSTOM_EFFECT_IMPLS
#include "print.h"

// The leds are numbered from 0 to 61
// starting at the top left going to the bottom right

// Top right is 0
// Top left is 13

// HE2023{LEDS_LIGHT_THE_WAY}
// H -> 34
// E -> 24
// 2 -> 11
// 0 -> 3
// 2 -> 11
// 3 -> 10
// { -> 16
// L -> 31
// E -> 24
// D -> 37
// S -> 38
// _ -> 2
// L -> 31
// I -> 19
// G -> 35
// H -> 34
// T -> 22
// _ -> 2
// T -> 22
// H -> 34
// E -> 24
// _ -> 2
// W -> 25
// A -> 39
// Y -> 21
// } -> 15

static uint8_t current;

static void flag_led_init(effect_params_t* params) {
  current = 0;

  for (uint8_t i = 0; i < 62; i++) {
    rgb_matrix_set_color(i, 0x00, 0x00, 0x00);
  }
}

static bool flag_led_run(effect_params_t* params) {
  static uint8_t flag_leds[] = { 34, 24, 11, 3, 11, 10, 16, 31, 24, 37, 38, 2, 31, 19, 35, 34, 22, 2, 22, 34, 24, 2, 25, 39, 21, 15};

  static uint32_t timer = 0;

  inline uint32_t interval(void) {
    return 3000 / scale16by8(qadd8(rgb_matrix_config.speed, 16), 16);
  }

  if (g_rgb_timer > timer) {
    rgb_matrix_set_color(flag_leds[current], 0x00, 0x00, 0x00);
    current = (current + 1) % (sizeof(flag_leds) / sizeof(uint8_t));
    RGB rgb = rgb_matrix_hsv_to_rgb(rgb_matrix_config.hsv);
    rgb_matrix_set_color(flag_leds[current], rgb.r, rgb.g, rgb.b);
    timer = g_rgb_timer + interval();
  }

  return rgb_matrix_check_finished_leds(62);
} // Our custom effect which shows the flag
static bool flag_led(effect_params_t* params) {
  if (params->init) { flag_led_init(params); }
  return flag_led_run(params);
}

#endif // RGB_MATRIX_CUSTOM_EFFECT_IMPLS
