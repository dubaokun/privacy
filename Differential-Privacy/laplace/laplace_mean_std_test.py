import numpy as np

def add_laplace_noise(data_list, μ=0, b=1):
    laplace_noise = np.random.laplace(μ, b, len(data_list)) # 为原始数据添加μ为0，b为1的噪声
    return laplace_noise + data_list

data = np.random.uniform(0, 100, 400)
print("原始无噪声数据|均值：" + str(data.mean()) + " 方差：" + str(data.std()))
noise_list = add_laplace_noise(data)
print("加噪声后的数据|均值：" + str(noise_list.mean()) + " 方差：" + str(noise_list.std()))
