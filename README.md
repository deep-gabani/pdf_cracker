# PDF Password Cracker [v1.0.4]

A python command line utility to crack open password-protected PDF files.


## Installation
It's recommended that you create a local python environment preferably with conda.

If you don't have conda installed, you can install using the following commands:
```shell
wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
bash Anaconda3-2020.07-Linux-x86_64.sh
```

Now, create a new conda env and activate it using the following commands:
```shell
conda create -n pdf_password_cracker -y python=3.8.5
conda activate pdf_password_cracker
```

Now, install the dependencies using the following command:
```shell
pip install -r requirements.txt
```


## Usage
```
usage: . [-h] -i INPUT_PDF -n PASSWORD_LENGTH [-l] [-d] [-sc] [-w]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_PDF, --input_pdf INPUT_PDF
                        Path of pdf file to crack.
  -n PASSWORD_LENGTH, --password_length PASSWORD_LENGTH
                        Password length.
  -l, --letters         Flag to indicate if there are letters in the password. Default = False.
  -d, --digits          Flag to indicate if there are digits in the password. Default = False.
  -sc, --special_chars  Flag to indicate if there are special characters in the password. Default = False.
  -w, --whitespace      Flag to indicate if there are whitespace in the password. Default = False.
```

Usage examples:
1. Cracking a pdf with password of length 5 and only digits.
```
python3 . \
    -i assets/5.pdf \
    -n 5 \
    -d
```

2. Cracking a pdf with password of length 4 and only letters.
```
python3 . \
    -i assets/7.pdf \
    -n 4 \
    -l
```

3. Cracking a pdf with password of length 4 with letters and digits.
```
python3 . \
    -i assets/7.pdf \
    -n 4 \
    -l \
    -d
```

4. Cracking a pdf with password of length 4 with letters, digits and special characters.
```
python3 . \
    -i assets/7.pdf \
    -n 4 \
    -l \
    -d \
    -sc
```

5. Cracking a pdf with password of length 4 with letters, digits, special characters and whitespaces.
```
python3 . \
    -i assets/7.pdf \
    -n 4 \
    -l \
    -d \
    -sc \
    -w
```

## Developers
Developed with ❤️  by [@deep-gabani](https://github.com/deep-gabani).