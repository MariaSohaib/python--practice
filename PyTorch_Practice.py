import torch
tensor0d=torch.tensor(1)
tensor1d=torch.tensor([1,2,3])
tensor2d=torch.tensor([[1,2],[2,3]])
print('\n',tensor0d.dtype)
print(tensor1d.shape)
print(tensor2d.reshape(1,4))   
T_tensor2d=tensor2d.T           #taking transpose of matrix
print(T_tensor2d)
print(tensor2d.matmul(T_tensor2d))          #Multiplying 2 Matrices