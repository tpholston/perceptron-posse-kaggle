# Kaggle 151B Competition

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/tpholston/perceptron-posse-kaggle.git
    ```

2. Create a virtual environment and activate it:

    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Upgrade pip:

    ```
    pip install --upgrade pip
    ```

4. Install the dependencies:

    ```
    pip install -r requirements.txt
    ```

5. Get data 

    There are two ways you can get the kaggle data. We can't keep it on github cause the files are too large. Either download it yourself and move it in or run get_kaggle_data.sh 

    If you download yourself, still create the folders and subsequently drop your data in data/raw_data:
    ```
    bash get_kaggle_data.sh -i
    ```
    Otherwise  run:
    ```
    bash get_kaggle_data.sh <kaggle-username> <kaggle-api-key>
    ```
    Or just use my kaggle info:
    ```
    bash get_kaggle_data.sh tylerholston 5462921d606a42072ea9b3d5006f7bea
    ```