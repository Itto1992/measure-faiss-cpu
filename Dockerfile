FROM continuumio/anaconda3

RUN conda install faiss-cpu==1.7.3 -c pytorch
RUN pip install fire
