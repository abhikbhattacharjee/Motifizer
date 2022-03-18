FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    libopenmpi-dev \
    openmpi-bin \
    ghostscript \
    libgs-dev \
    libgd-dev \
    libexpat1-dev \
    zlib1g-dev \
    libxml2-dev \
    autoconf automake libtool \
    libhtml-template-compiled-perl \
    libxml-opml-simplegen-perl \
    libxml-libxml-debugging-perl \
    sudo \
    openssh-server

RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install Log::Log4perl'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install Math::CDF'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install CGI'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install HTML::PullParser'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install HTML::Template'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Simple'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Parser::Expat'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::LibXML'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::LibXML::Simple'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Compile'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Compile::SOAP11'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Compile::WSDL11'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Compile::Transport::SOAPHTTP'
RUN mkdir /opt/meme
ADD http://meme-suite.org/meme-software/5.0.4/meme-5.0.4.tar.gz /opt/meme
WORKDIR /opt/meme/
RUN tar zxvf meme-5.0.4.tar.gz && rm -fv meme-5.0.4.tar.gz
RUN cd /opt/meme/meme-5.0.4 && \
	./configure --prefix=/opt  --enable-build-libxml2 --enable-build-libxslt  --with-url=http://meme-suite.org && \ 
	make && \
	make install && \
        rm -rfv /opt/meme

ARG PACKAGE_VERSION=2.27.1
ARG BUILD_PACKAGES="git openssl python build-essential zlib1g-dev"
ARG DEBIAN_FRONTEND=noninteractive

# Update the repository sources list
RUN apt-get update && \
    apt-get install --yes \
              $BUILD_PACKAGES && \
    cd /tmp && \
    git clone https://github.com/arq5x/bedtools2.git && \
    cd bedtools2 && \
    git checkout v$PACKAGE_VERSION && \
    make && \
    mv bin/* /usr/local/bin && \
    cd / && \
    rm -rf /tmp/* && \
    apt remove --purge --yes \
              $BUILD_PACKAGES && \
    apt autoremove --purge --yes && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*
    
#FROM python:3.6
#RUN pip install flask        

# wget to 1.17.1
RUN echo "Package: wget\nPin: version 1.17.1*\nPin-Priority: 1000" > /etc/apt/preferences.d/wget

# unzip to 6.0-20
RUN echo "Package: unzip\nPin: version 6.0-20*\nPin-Priority: 1000" > /etc/apt/preferences.d/unzip

# python to 2.7.11
RUN echo "Package: python\nPin: version 2.7.11*\nPin-Priority: 1000" > /etc/apt/preferences.d/python

# build-essential to 12.1
RUN echo "Package: build-essential\nPin: version 12.1*\nPin-Priority: 1000" > /etc/apt/preferences.d/build-essential

RUN apt-get update && apt-get -y install \
    wget \
    unzip \
    python \
    build-essential

WORKDIR /opt

RUN wget ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/downloads/hisat2-2.1.0-source.zip && unzip hisat2-2.1.0-source.zip && cd hisat2-2.1.0 && make && rm /opt/hisat2-2.1.0-source.zip

ENV PATH "$PATH:/opt/hisat2-2.1.0/"

RUN apt-get update && apt-get -y upgrade && \
	apt-get install -y build-essential wget \
		libncurses5-dev zlib1g-dev libbz2-dev liblzma-dev libcurl3-dev && \
	apt-get clean && apt-get purge && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /usr/src

#Samtools
RUN wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 && \
	tar jxf samtools-1.9.tar.bz2 && \
	rm samtools-1.9.tar.bz2 && \
	cd samtools-1.9 && \
	./configure --prefix $(pwd) && \
	make

ENV PATH=${PATH}:/usr/src/samtools-1.9 


RUN apt-get update && \
    apt-get install -y r-base && \
    apt-get install -y wget && \
    apt-get install perl

# R is already installed and ready, install the edgeR package and the dependencies
WORKDIR /tmp
RUN wget https://github.com/bioneos/docker-containers/raw/master/edgeR/src/edgeR_3.20.2.tar.gz && \
  tar zxvf edgeR_3.20.2.tar.gz
RUN wget https://github.com/bioneos/docker-containers/raw/master/edgeR/src/limma_3.34.4.tar.gz && \
  tar zxvf limma_3.34.4.tar.gz
RUN wget https://github.com/bioneos/docker-containers/raw/master/edgeR/src/locfit_1.5-9.1.tar.gz && \
  tar zxvf locfit_1.5-9.1.tar.gz
RUN wget https://github.com/bioneos/docker-containers/raw/master/edgeR/src/Rcpp_0.12.14.tar.gz && \
  tar zxvf Rcpp_0.12.14.tar.gz

RUN R -e "install.packages(c('/tmp/limma', '/tmp/locfit', '/tmp/Rcpp', '/tmp/edgeR'), repos = NULL, type = 'source')"

# Default command
CMD /bin/bash

RUN apt-get update && \
    apt-get install -y bwa && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip

RUN apt-get install -y python-pip    
RUN pip install --upgrade pip  && \
    pip install numpy  

RUN pip install MACS2==2.1.4
    #pip install PePr 
    #pip3 install -y homer
    
    
WORKDIR /tmp1
RUN wget http://homer.ucsd.edu/homer/configureHomer.pl
RUN perl configureHomer.pl -install
ENV PATH="/tmp1/bin:${PATH}"
RUN perl configureHomer.pl -install dm6

RUN pip install flask
EXPOSE 5000
    
RUN apt-get install -y protobuf-compiler python-pil python-lxml
RUN pip install jupyter
RUN pip install matplotlib
RUN pip install tensorflow

RUN pip install pandas
RUN pip install xlrd
RUN sudo apt-get install -y parallel
RUN pip install openpyxl
RUN pip install keras
RUN pip install scikit-learn

RUN pip install 'HTSeq==0.12.3'

ENV PATH="/opt/bin:${PATH}"
RUN adduser --disabled-password --gecos '' motifizer
RUN adduser motifizer sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER motifizer
COPY . /home/motifizer
CMD /bin/bash
WORKDIR /home/motifizer
