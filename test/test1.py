import torch
print(torch.version.cuda)
print(torch.backends.cudnn.version())
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("GPU:", torch.cuda.get_device_name())
else:
    device = torch.device("cpu")
    print("No GPU available, using CPU instead.")
