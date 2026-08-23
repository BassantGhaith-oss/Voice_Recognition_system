# Voice_Recognition_system

This project represents a small voice recognition system.

In case of saying commands such as "open Google", "open YouTube", "open calculator", "open Notepad", "exit", or "time", the project executes the corresponding command.

This project depends on understanding the following steps:
1. Recording the voice and saving it in a file with a `.wav` extension → using libraries such as `sounddevice` and `wavio`.
2. STT (Speech-to-Text) is the second step → using Whisper AI model to convert the recorded audio into text.
3. Using the text command obtained from the previous step to execute a specific action → this could be used to manage an electronic device, such as in IoT.
The operations, such as recording, saving the WAV file, transcribing the file, and executing commands, are preferably defined as functions to be called later.
