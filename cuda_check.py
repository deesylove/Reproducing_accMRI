
def cuda_check():
  import torch
  if torch.cuda.is_available():
    device = torch.device("cuda:0")
    print("GPU")
  else: 
    device = torch.device("cpu")
    print("CPU")
'''
def tf_check():
  import tensorflow as tf
  print(tf.config.list_physical_devices('GPU'))

'''
def main():
  print("cuda_check")
  cuda_check()

if __name__ == "__main__":
    main()