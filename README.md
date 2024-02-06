# SSL-speechdepressiondetection

Exploring Self-Supervised Models for Depressive Disorder Detection: A Study on Speech Corpora (submitted in EMBC-24)


Codes (Depression Classification task in Indic-Bengali Language):
- **pre-process/augmentation.py:** data augmentation technique with window size of 3 sec and an overlap of 50% to divide the audio into several segments.
- **pre-process/features.py:** extract mfcc and mel-spectrogram features.
-  **HubERT.py:** train and test with pre-trained Hubert network and classify with ML classifiers.
-  **Wav2Vec2.0.py:** train and test with pre-trained Wav2Vec2.0 network and classify with ML classifiers.
-  **WavLM.py:** train and test with pre-trained WavLM network and classify with ML classifiers.
