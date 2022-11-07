import tensorflow as tf
# print("Tensorflow version:", tf.__version__)

tensor1 = tf.constant([3, 4, 5])
tensor2 = tf.constant([6, 7, 8])
# print(tensor1 + tensor2)

tensor3 = tf.constant([[1, 2], [3, 4]])

# 연산
# print(tf.add(tensor1, tensor2))
# tf.subtract(), tf.divide(), tf.multiply()
# tf.matmul() : dot product

# 0만 가득한 tensor
tensor4 = tf.zeros([2, 2, 3])
# print(tensor4)

# shape
print(tensor4.shape)

# variable
w = tf.Variable(1.0)

## w.numpy() : 변수의 값
print(w.numpy())

## w.assign() : 변수에 새로운 값 대입
w.assign(2)
print(w)

# 딥러닝으로 간단한 수학문제 풀어보기
키 = 170
신발 = 260
# 신발 = 키 * a + b

a = tf.Variable(0.1)
b = tf.Variable(0.2)

## 손실함수 : mean squared error / binary cross entropy
def 손실함수():
    return tf.square(신발 - (키 * a + b))

## 경사하강법으로 a, b 구하기
opt = tf.keras.optimizers.Adam(learning_rate=0.1)

for i in range(300): 
    opt.minimize(손실함수, var_list=[a, b])
    # print(a.numpy(), b.numpy())

print(170 * 1.52 + 1.62)