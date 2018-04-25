bazel run test_streaming_accuracy -- \
--graph=/tmp/speech_commands_train_20180321-161243.pb \
--labels=/tmp/speech_commands_train/conv_labels.txt \
--wav=/format_convert/data/t1_20180410.wav \
--verbose
