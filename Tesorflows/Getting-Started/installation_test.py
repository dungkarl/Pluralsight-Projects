import tensorflow as tf


session = tf.Session()

# Verify we can print a string
hello = tf.constant("Hello Pluralsight from TensorFlow")
print(session.run(hello))

#   Perform some simple math
a = tf.constant(20)
b = tf.constant(22)
print('a + b = {0}'.format(session.run(a + b)))