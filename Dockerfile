FROM python:3.9

ADD compute.py .
ADD generate_data.py .

RUN pip install numpy

CMD python generate_data.py ; cat input_file.txt | python compute.py
