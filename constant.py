import os

rootPath = r"C:\Users\as116\OneDrive - Indian Institute of Technology Bombay\Documents B\Sem 7\IE643\IE643_180260004_CHALLENGE"
dataset_dir = r".\dataset"
image_dir = r".\spectrograms"
train_dir = image_dir + "\train"
test_dir = image_dir + "\test"
val_dir = image_dir + "\val"
model_dir = r".\model\IE643_180260004_CHALLENGE_MODEL.pt"
zippath = r".\dataset.zip"
audio_dir = os.path.join(dataset_dir, "challenge_dataset")
labels_dir = [os.path.join(audio_dir, i) for i in os.listdir(audio_dir)]

num_of_augments = 50

input_features = 257
n_fft = 2 * (input_features - 1)
hop_length = 256
win_length = 512
