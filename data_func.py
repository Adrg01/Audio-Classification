import librosa
import time
import sounddevice as sd
import numpy as np
from zipfile import ZipFile
from constant import *


def load_files(zippath=zippath):

    try:
        extract_file = ZipFile(zippath, "r")
        extract_file.extractall()
    except:
        pass
    finally:
        print("Extraction Finished.")

    data = []
    labels = []
    filenames = []
    for i, path in enumerate(labels_dir):
        for file in os.listdir(path):
            # file = os.path.join(path,file)
            audio_data, sample_rate = librosa.load(
                "{}/{}".format(path, file), mono=True
            )
            sr = sample_rate
            data.append(audio_data)
            labels.append(i + 1)
            filenames.append(str(i + 1) + "\\" + file)
    data = np.array(data)
    print("Data loaded")
    print("Data shape : ", data.shape)
    return data, labels, filenames, sr


def normalize(data):
    for i, sound in enumerate(data):
        data[i] = librosa.util.normalize(sound)


def trim_data(data, top_db=20, hop_length=4):
    for i, sound in enumerate(data):
        data[i], _ = librosa.effects.trim(sound, top_db=top_db, hop_length=hop_length)
    # return data


def play_all_sounds(waveforms, sr):
    for wf in waveforms:
        sd.play(wf, sr)
        time.sleep(2)


def stft_array(data):
    stft_data = []
    for sound in data:
        stft_data.append(
            np.abs(
                librosa.stft(
                    sound, n_fft=n_fft, hop_length=hop_length, win_length=win_length
                )
            )
        )
    return stft_data
