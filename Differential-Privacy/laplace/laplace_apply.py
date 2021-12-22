import numpy as np
 
# 计算基于拉普拉斯分布的噪声
def laplace_noisy(sensitivety,epsilon):
    n_value = np.random.laplace(0, sensitivety/epsilon, 1)
    return n_value

# 基于laplace的分布函数的反函数计算
def laplace_noisy2(sensitivety, epsilon):
    b = sensitivety/epsilon
    u1 = np.random.random()         # Return random floats in the half-open interval [0.0, 1.0).
    # u2 = np.random.random()         # Return random floats in the half-open interval [0.0, 1.0).
    # print("u1 = %.16f and u2 = %.16f" % (u1, u2))
    if u1 <= 0.5:
        noisy = -b*np.log(1.-u1)
    else:
        noisy = b*np.log(u1)
    return noisy

def laplace_noisy3(x,beta):
 result = (1/(2*beta)) * np.e**(-1*(np.abs(x)/beta))
 return result

# 计算基于拉普拉斯加噪的混淆值
def laplace_mech(data, sensitivety, epsilon):
    for i in range(len(data)):
        # data[i] += laplace_noisy(sensitivety,epsilon)
        data[i] += laplace_noisy2(sensitivety,epsilon)
    return data
 
# 基于拉普拉斯分布的特性，如果想要分布震荡较小，需要将隐私预算epsilon的值设置较大
if __name__ =='__main__':
    while(True):
      data = [1.,2.,3.]
      sensitivety = 1
      epsilon = 100
      data_noisy = laplace_mech(data, sensitivety, epsilon)
      for j in data_noisy:
          print("Final Resulet = %.16f" % j)
      break
