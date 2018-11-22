FROM python:latest

RUN git clone git://github.com/dajobe/raptor.git
WORKDIR raptor
RUN ./autogen.sh
RUN make
RUN make check
RUN make install

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/