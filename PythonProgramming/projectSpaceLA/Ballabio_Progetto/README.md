# 
- - - -
## 📒 Table of Contents
* [📍 Overview](#-overview)
* [⚙️ Features](#-features)
* [📂 Project Structure](#project-structure)
* [🧩 Modules](#modules)
* [🚀 Getting Started](#-getting-started)
* [🗺 Roadmap](#-roadmap)
* [🤝 Contributing](#-contributing)
* [📄 License](#-license)
* [👏 Acknowledgments](#-acknowledgments)

- - - -
## 💡 Overview 
Il Progetto SpaceLA, dove LA significa SpaceLaunches, è stato il mio esame finale del corso di Python Programming, del corso di ML & AI presso l’ITS Angelo Rizzoli.

L’esame consisteva nello sviluppo di un programma in python che avesse le seguente caratteristiche:

1. web scraping con Beautiful Soup
2. analisi dati con Pandas, e opzionalmente Numpy
3. visualizzazione dei dati di output

Nel mio caso mi sono divertito ad analizzare i dati dei lanci spaziali da wikipedia (https://en.wikipedia.org/wiki/Timeline_of_spaceflight) [link](https://en.wikipedia.org/wiki/Timeline_of_spaceflight).

- - - -
## ⚙️ Features
Nel dettaglio, il programma permette di scegliere un anno dal 1951 ad oggi e di visualizzare alcune statistiche:

* numero di lanci di quell’anno
* funzione dei lanci (ad esempio: Missile Test, Aeronomy, Biological, … )
* esito dei lanci (successful, failure, partial failure)

- - - -
## 📂 Project Structure

```bash
repo
├── LICENSE
├── ProjectSpaceLA.ipynb
├── functions.py
└── main.py

1 directory, 4 files
```

Il notebook jupyter`ProjectSpaceLA.ipynb` è comodo per visualizzare gli output del programma a ogni operazione; inoltre, è stato utile a scopo di presentazione del progetto.

- - - -
## 🚀 Getting Started
### 📦 Installation

1. Clone the repository:
```sh
git clone
```

2. Change to the project directory:
```sh
cd
```

### 🎮 Use
1. Run the `main.py` script
```sh
python main.py
```

2. Run with `Jupyter Lab`
```sh
jupyter-lab # inside the project directory
```

- - - -
## ⚠️ Known Issues

* Some launches are mistakenly marked as failures because the corresponding cell in the Wikipedia table is empty.
* The date format is not standard (timestamp), and I wasn’t able to fix it.
* It works fine with the year 1951. However, for example, with the year 1960, it gives an error.

### Disclaimer
I wrote the code the afternoon before the exam :D
- - - -
## 🤝 Contributing
Contributions are always welcome! 

Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

- - - -
## 📄 License
This project is licensed under the `MIT` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

- - - -
## 👏 Acknowledgments

> * `ℹ️  List any resources, contributors, inspiration, etc.`  

- - - -