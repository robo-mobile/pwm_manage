def_config = '''

title = "PWM manager config"

pwm_type = "L9110S"             # choose  one of: L9110S/L298N/DL298N (double DL298N)

log_level = "INFO"              # EMERGENCY/ALERT/CRITICAL/ERROR/WARNING/NOTICE/INFO/DEBUG

# standat pwm engine type

# [outputs]
# channel1 = 36
# channel2 = 37
# channel3 = 38
# channel4 = 39

# l298n engine type

# [outputs]
# enA = 35
# channel1 = 36
# channel2 = 37
# enB = 40
# channel3 = 38
# channel4 = 39

# double l298n engine type

# [outputs]
# enA1 = 40
# channel11 = 38
# channel12 = 36
# enB1 = 33
# channel13 = 35
# channel14 = 37
# enA2 = 32
# channel21 = 31
# channel22 = 29
# enB2 = 26
# channel23 = 27
# channel24 = 28
'''

