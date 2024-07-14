from scipy.io import wavfile
from pesq import pesq
 
# Load the reference and degraded audio files

sr_ref, ref = wavfile.read("./ref_16K.wav")
sr_deg1, deg1 = wavfile.read("./deg1_30_skype_16K.wav")
sr_deg2, deg2 = wavfile.read("./deg2_30_skype_16K.wav")
sr_deg3, deg3 = wavfile.read("./deg3_30_skype_16K.wav")
 
# Ensure the sampling rates match

assert sr_ref == sr_deg1
mos_score1 = pesq(ref=ref, deg=deg1, fs=sr_ref, mode='nb')
print(f"PESQ MOS score 1: {mos_score1}")

assert sr_ref == sr_deg2
mos_score2 = pesq(ref=ref, deg=deg2, fs=sr_ref, mode='nb')
print(f"PESQ MOS score 2: {mos_score2}")

assert sr_ref == sr_deg3
mos_score3 = pesq(ref=ref, deg=deg3, fs=sr_ref, mode='nb')
print(f"PESQ MOS score 3: {mos_score3}") 

print(f"Avg PESQ MOS score: {(mos_score1+mos_score2+mos_score3)/3}") 