# Project SpaceLA
- - - -
## 📒 Table of Contents
* [💡 Overview](#-overview)
* [⚙️ Features](#-features)
* [📂 Project Structure](#-project-structure)
* [🚀 Getting Started](#-getting-started)
* [⚠️ Known Issues](#-known-issues)
* [🤝 Contributing](#-contributing)
* [📄 License](#-license)
* [👏 Acknowledgments](#-acknowledgments)

- - - -
## 💡 Overview
The SpaceLA Project, where LA stands for SpaceLaunches, was my final exam for the Python Programming course and the ML & AI course at VET Angelo Rizzoli.

The exam involved developing a Python program with the following features:

1. Web scraping using Beautiful Soup
2. Data analysis with Pandas, and optionally Numpy
3. Visualization of the output data

In my case, I enjoyed analyzing space launch data from [Wikipedia](https://en.wikipedia.org/wiki/Timeline_of_spaceflight).

- - - -
## ⚙️ Features
In detail, the program allows you to choose a year from 1951 to the present and view some statistics:

* Number of launches for that year
* Types of launches (for example: Missile Test, Aeronomy, Biological, ...)
* Outcomes of launches (successful, failure, partial failure)

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

The Jupyter notebook `ProjectSpaceLA.ipynb` is convenient for viewing the program's outputs after each operation. Additionally, it was useful for the purpose of presenting the project.

- - - -
## 🚀 Getting Started
### 📦 Installation

1. Clone the repository:
```sh
git clone https://github.com/enaikey00/School-Stuff.git
```

2. Change to the project directory:
```sh
cd School-Stuff/PythonProgramming/projectSpaceLA
```

### 🎮 Use
Run the `main.py` script
```sh
python main.py
```
or

Run with `Jupyter Lab`
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

> Inspiration: my passion for space

- - - -
