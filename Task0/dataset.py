from attributes import *

dataset = {
    (SUN,      HOT,   HIGH,   LOW)  :  False,
    (SUN,      HOT,   HIGH,   HIGH) :  False,
    (OVERCAST, HOT,   HIGH,   LOW)  :  True,
    (RAIN,     SWEET, HIGH,   LOW)  :  True,
    (RAIN,     COLD,  NORMAL, LOW)  :  True,
    (RAIN,     COLD,  NORMAL, HIGH) :  False,
    (OVERCAST, COLD,  NORMAL, HIGH) :  True,
    (SUN,      SWEET, HIGH,   LOW)  :  False,
    (SUN,      COLD,  NORMAL, LOW)  :  True,
    (RAIN,     SWEET, NORMAL, LOW)  :  True,
    (SUN,      SWEET, NORMAL, HIGH) :  True,
    (OVERCAST, SWEET, HIGH,   HIGH) :  True,
    (OVERCAST, HOT,   NORMAL, LOW)  :  True,
    (RAIN,     SWEET, HIGH,   HIGH) :  False
}