import tensorflow as tf

### DATA FILES CONST
# CSV header
KEYS = ["t","aa.x","aa.y","aa.z","aReal.x","aReal.y","aReal.z"]
KEY_COUNT = len(KEYS)

# Standard keys used
STANDARD_KEYS = ["t","aa.x","aa.y","aa.z"]
STANDARD_KEY_COUNT = len(STANDARD_KEYS)

# How many points should be read from the data
DATA_LENGTH = 400

# How many commands currently supported
COMMAND_COUNT = 2

# Noise Command 
NOISE_FILE_PREFIX = "noise_"
NOISE_FILE_LABEL  = tf.reshape([1, 0], [1, COMMAND_COUNT])

# Focus Command
FOCUS_FILE_PREFIX = "focus_"
FOCUS_FILE_LABEL  = tf.reshape([0, 1], [1, COMMAND_COUNT])
