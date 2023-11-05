# Syllabus
## Concetti fondamentali di reti neurali
+ Neurone computazionale
+ funzioni di attivazione (es. sigmoide e ReLU)
+ Strato denso
+ MultiLayer Perceptron
+ Minibatch gradient descent
+ Dropout
+ Batch Normalization

## Reti convoluzionali e computer vision
+ Filtri
+ Strati convoluzionali
+ Strati di pooling
+ Struttura di una rete convoluzionale classica (tipo LeNet5)
+ Resnet e skip connection
+ Data augmentation
+ Transfer learning
+ Reti per segmentazione

## Reti ricorrenti, transformer e NLP
+ Strati ricorrenti, LSTM e GRU
+ Ricorrenti multistrato
+ Concetto e strato di embedding Embedding
+ Tokenizzazione (esempi di subword tokenization: BPE e WordPiece)
+ Modelli di linguaggio
+ Architettura Encoder-Decoder basata su reti ricorrenti
+ Transformer encoder (BERT)
+ Q&A con Huggingface e Haystack

## Librerie e tool
### Tensorflow
+ Tensori
+ Variabili
+ TapeGradient
### Keras
+ Costruzione di un modello con classe Sequential
+ Costruzione di un modello tramite sottoclasse
### Callbacks
+ EarlyStopping
+ ModelCheckpoint
+ Tensorboard
+ CSVLogger
+ compilazione
+ fit (con tensori oppure oggetti Dataset di Tensorflow)
### Huggingface
+ Libreria tokenizers
+ Libreria datasets
+ Libreria transformers

## Alcune risorse
+ [Deep Learning with Python](https://www.manning.com/books/deep-learning-with-python) (manning.com) scritto da Francois Chollet, creatore di Keras. Ottima introduzione al Deep Learning, Tensorflow e Keras di  taglio applicativo (poca matematica)
+ [Dive into Deep Learning — Dive into Deep Learning 1.0.3 documentation (d2l.ai)](https://d2l.ai/). La bibbia del Deep Learning. Librone con tutti i concetti fondamentali del DL e implementazioni from scratch delle principali architetture neurali (in Tensorflow, PyTorch e altri framework). C’è un po’ di matematica…
+ [DeepLearning.AI: Start or Advance Your Career in AI](https://www.deeplearning.ai/). I corsi di Andrew Ng. Dalle basi a concetti abbastanza avanzati.
+ [Natural Language Processing with Transformers, Revised Edition](https://www.oreilly.com/library/view/natural-language-processing/9781098136789/) (oreilly.com). Ottimo libro su NLP, Transformers e Huggingface. Esempi sui principali task di NLP
+ [Generative Deep Learning, 2nd Edition](https://www.oreilly.com/library/view/generative-deep-learning/9781098134174/) (oreilly.com). Panoramica su Deep Learning generativo
+ [Introduction - Hugging Face NLP Course](https://huggingface.co/learn/nlp-course/chapter1/1) Corso di NLP e Hugginface.
+ [huggingface/diffusion-models-class: Materials for the Hugging Face Diffusion Models Course](https://github.com/huggingface/diffusion-models-class) (github.com) Corso di Huggingface sui modelli di diffusione.
