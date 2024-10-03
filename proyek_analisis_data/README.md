Setup Environment - Anaconda

conda create --name main-ds python=3.9
conda activate main-ds
pip install matplotlib
pip install pandas
pip install streamlit

Setup Environment - Shell/Terminal

mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install matplotlib
pip install pandas
pip install streamlit

Run steamlit app

streamlit run dashboard.py

or

streamlit run /proyek_analisis_data/dasboard/dashboard.py
