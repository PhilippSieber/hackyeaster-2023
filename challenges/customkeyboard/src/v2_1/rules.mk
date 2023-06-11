# MCU name
MCU = atmega32u4

# Bootloader selection
BOOTLOADER = lufa-ms
BOOTLOADER_SIZE = 6144

LAYOUTS = 60_ansi

# Build Options
#   change yes to no to disable
#
BOOTMAGIC_ENABLE = yes      # Enable Bootmagic Lite
MOUSEKEY_ENABLE = no          # Mouse keys
EXTRAKEY_ENABLE = no          # Audio control and System control
COMMAND_ENABLE = no            # Commands for debug and configuration
NKRO_ENABLE = no           # Enable N-Key Rollover
BACKLIGHT_ENABLE = no          # Enable keyboard backlight functionality
RGBLIGHT_ENABLE = no           # Enable keyboard RGB underglow
AUDIO_ENABLE = no              # Audio output
RGB_MATRIX_ENABLE = yes        # Use RGB matrix
RGB_MATRIX_DRIVER = IS31FL3733
RGB_MATRIX_CUSTOM_USER = yes
CONSOLE_ENABLE = yes
LTO_ENABLE = yes
