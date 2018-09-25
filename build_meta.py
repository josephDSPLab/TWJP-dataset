'''Simple I/O tool for TW-JP project
'''
import librosa
import os
import numpy as np
from ruamel import yaml

def read_all(dir_p):
    '''
    dir_p, path for the directory of the *.wav files.
    '''
    files = os.listdir(dir_p)
    max_len = min_len = np.inf
    file_count = 0
    tot_dur = 0
    for f in files:
        print(f)
        if '.wav' not in f:
            continue
        else:
            f_path = os.path.join(dir_p, f)
            file_count += 1
        a, fs = librosa.load(f_path, sr=None, mono=False)
        dur = float(a.shape[1]) / fs
        tot_dur += dur
        if np.isinf(max_len):
            max_len = min_len = dur
        elif dur > max_len:
            max_len = dur
        elif dur < min_len:
            min_len = dur
    return round(min_len, 2), round(max_len, 2), file_count, round(tot_dur, 2)

if __name__ == '__main__':
    min_dur, max_dur, f_count, tot_dur = read_all('audio/')

    if os.path.exists('metadata.yaml'):
        with open('metadata.yaml', 'r') as stream:
            org_dict = yaml.load(stream, Loader=yaml.RoundTripLoader)
        if org_dict is None:
            os.remove('metadata.yaml')
        else:
            org_dict['recodings_number'] = f_count
            org_dict['tot_dur'] = tot_dur
            org_dict['min_dur'] = min_dur
            org_dict['max_dur'] = max_dur

            change_dump = yaml.dump(
                org_dict, default_flow_style=False, Dumper=yaml.RoundTripDumper)
            with open('metadata.yaml', 'w') as stream:
                stream.write(change_dump)
    if not os.path.exists('metadata.yaml'):
        with open('metadata.yaml', 'w') as stream:
            init_dump = yaml.dump(
                {'recodings_number': f_count,
                 'tot_dur': tot_dur,
                 'min_dur': min_dur,
                 'max_dur': max_dur}, default_flow_style=False, Dumper=yaml.RoundTripDumper)
            stream.write(init_dump)
