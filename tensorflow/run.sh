bazel run tensorflow/examples/speech_commands:test_streaming_accuracy -- \
--graph=/tmp/speech_commands_train_20180321-161243.pb \
--labels=/tmp/speech_commands_train/conv_labels1.txt \
--wav=/root/test/format_convert/output/test3_standard.wav \
--verbose
