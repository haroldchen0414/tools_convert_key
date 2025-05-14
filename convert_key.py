# -*- coding: UTF-8 -*-
# author: haroldchen0414
# python 3.9.13 music21 8.3.0

from music21 import converter, key, interval

midiFile = converter.parse("Taylor Swift - Back to December.mid")
originalKey = midiFile.analyze("key")

if originalKey is None:
    raise ValueError("无法分析midi文件原来的调号")

print("原调号:", originalKey)

# 使用说明
# key.Key("C") # C大调
# key.Key("a") # a小调
# key.Key("a#") # a#小调
# key.Key("3") # 3个升号的大调
# key.Key("-4") # 4个降号的大调
# key.Key("D", "major") # D大调
# key.Key("E", "minor") # E小调
# key.Key("Fb") # 降F
targetKey = key.Key("Fb")

transpositionInterval = interval.Interval(originalKey.tonic, targetKey.tonic)
print("转调音程:", transpositionInterval)

transpositionIntervalMidi = midiFile.transpose(transpositionInterval)
transpositionIntervalMidi.write("midi", "Taylor Swift - Back to December_Fb.mid")

