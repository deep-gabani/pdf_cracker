# PDF Cracker [v2.0.1]

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
conda create -n pdf_cracker -y python=3.8.5
conda activate pdf_cracker
```

Now, install the dependencies using the following command:
```shell
pip install -r requirements.txt
```


## Usage

```
usage: . [-h] -i INPUT_PDF -n PASSWORD_LENGTH [-l] [-u] [-d] [-sc] [-w] [-t THREADS]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_PDF, --input_pdf INPUT_PDF
                        Path of pdf file to crack.
  -n PASSWORD_LENGTH, --password_length PASSWORD_LENGTH
                        Password length.
  -l, --lower_letters   Flag to indicate if there are lower case letters in the password. Default = False.
  -u, --upper_letters   Flag to indicate if there are upper case letters in the password. Default = False.
  -d, --digits          Flag to indicate if there are digits in the password. Default = False.
  -sc, --special_chars  Flag to indicate if there are special characters in the password. Default = False.
  -w, --whitespace      Flag to indicate if there are whitespace in the password. Default = False.
  -t THREADS, --threads THREADS
                        Number of threads to use.
```

Usage examples:
1. Cracking a pdf with password of length 5 and only digits.
```
python3 . \
    -i assets/5.pdf \
    -n 5 \
    -d
```

2. Cracking a pdf with password of length 4 and only lower case letters.
```
python3 . \
    -i assets/7.pdf \
    -n 4 \
    -l
```

3. Cracking a pdf with password of length 4 and only upper case letters.
```
python3 . \
    -i assets/7.pdf \
    -n 4 \
    -u
```

4. Cracking a pdf with password of length 4 with lower case letters and digits.
```
python3 . \
    -i assets/7.pdf \
    -n 4 \
    -l \
    -d
```

5. Cracking a pdf with password of length 4 with lower case letters, digits and special characters.
```
python3 . \
    -i assets/7.pdf \
    -n 4 \
    -l \
    -d \
    -sc
```

6. Cracking a pdf with password of length 4 with lower case letters, digits, special characters and whitespaces.
```
python3 . \
    -i assets/7.pdf \
    -n 4 \
    -l \
    -d \
    -sc \
    -w
```

7. Cracking a pdf with password of length 4 with letters, digits, special characters and whitespaces with 5 threads parallely.
If you do not provide additional pipeline arguments, it will by default run locally (using DirectRunner).
```
python3 . \
    -i assets/7.pdf \
    -n 4 \
    -l \
    -d \
    -sc \
    -w \
    -t 5
```

7. Cracking a pdf with password of length 4 with letters, digits, special characters and whitespaces with 5 threads parallely on GCP.
```
python3 . \
    -i assets/7.pdf \
    -n 4 \
    -l \
    -d \
    -sc \
    -w \
    -t 5 \
    --runner DataflowRunner \
    --project MyProjectName \
    --region MyRegion \
    --temp_location MyTempBucketLocation \
    --job_name MyJobName

```


## Performance

Depending on the hardware capapbilities, performace can vary.

On my 12 core, 16GB DDR4 RAM and with 10 threads, it took about 08:23 minutes to crack open `assets/2.pdf` with password `oops`.
Exact command I used was:
```bash
python3 . \
    -i assets/2.pdf \
    -l \
    -n 4 \
    -t 10
```


## Developers
Developed with ❤️  by [@deep-gabani](https://github.com/deep-gabani).