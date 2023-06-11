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
    
6. Get Data (updated)
    
    With the computational complexity of filtering out data points of cars going over a threshold of mph we decided to put the training dataset on google drive. This is the link:
    https://drive.google.com/file/d/1Il-Yny9w0PmSMmvqCWM8fqAxM8bBQe4P/view?usp=sharing
    
7. Run model
    
    1. run rf_calltype_A.ipynb
    2. run rf_calltype_B.ipynb
    3. run rf_calltype_C.ipynb
    4. concate predictions with concatenate.ipynb

8. Pre-trained models

    If you want to load in a pre-trained model (they are rather large files even compressed but knock yourself out) you can access the joblib dumps here:
    
    rf calltype A: https://drive.google.com/file/d/1c4BVu6p-TFTK3WAR7KHhw-XVa8A6AdbT/view?usp=sharing
    
    rf calltype B: https://drive.google.com/file/d/1-dnjLbnufSWMwXbPjlFgU2lcxqxGmUt3/view?usp=sharing
    
    rf calltype C: https://drive.google.com/file/d/1wvXh3a9RCaNCES32bugV5j0ZoeqIJ6ij/view?usp=sharing
