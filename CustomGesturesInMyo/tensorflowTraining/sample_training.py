# data.txt - Hand open
# data1.txt - Fist close
# data2.txt - Single Finger
# data3.txt - Two Finger
# data4.txt - Three Finger
import tensorflow as tf

dataSets = ["data4.txt","t_data4.txt","t2_data4.txt","t3_data4.txt","t4_data4.txt"]
parentDirecotry = "/Users/phil/Documents/ML-Projects/CustomGesturesInMyo/tensorflowTraining/"

sensor1 = tf.placeholder(dtype=tf.int32, shape=(1,9))
sensor2 = tf.placeholder(dtype=tf.int32, shape=(1,9))
sensor3 = tf.placeholder(dtype=tf.int32, shape=(1,9))
sensor4 = tf.placeholder(dtype=tf.int32, shape=(1,9))
sensor5 = tf.placeholder(dtype=tf.int32, shape=(1,9))
sensor6 = tf.placeholder(dtype=tf.int32, shape=(1,9))
sensor7 = tf.placeholder(dtype=tf.int32, shape=(1,9))
sensor8 = tf.placeholder(dtype=tf.int32, shape=(1,9))

for file in dataSets:
    print(parentDirecotry+file)

sess = tf.Session()
print("Session Created..")
init = tf.initialize_all_variables()
sess.run(init)
print("Session Running..")
