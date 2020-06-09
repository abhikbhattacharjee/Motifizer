# Motifizer
Motifizer is a gene expression regulation predictor, a project that will address the problem of finding gene regulatory patterns and prove to be a useful tool for the researchers by simplifying the troubles involved in their jobs by optimizing the pre-existing processes to make them cost and time-efficient alongside providing deep conclusive insights about their data.
Motifizer is comprised of four major modules:
- Analysis Module (Provides a conclusive result about the count frequency analysis for a particular motif in a given type of regulation)
- ChIP-Seq Module (Efficiently carries out the computational process of ChIP-Seq Analysis)
- RNA-Seq Module (Efficiently carries out the computational process of RNA-Seq Analysis. Comprises of Hisat2 as well as EdgeR analysis) 
- Prediction Module (To effeciently predict the possible regulation of a given sequence)

## Developed By
- Abhik Bhattacharjee (abhik.bhattacharjee16@gmail.com)
- Pranav Badhe (badhepranav@gmail.com)
- Chinmay Dongaonkar (chinmaydongaonkar1998@gmail.com)
- Yash Gaglani (yashsuccessredefined@gmail.com)
- Soumen Khan (soumenkhan123@gmail.com)

We would be happy to address any issues faced while testing and deployment of the source code on the end-users' device, which will make our code more robust and consistent. You can raise an issue on Github or contact us on the provided email addresses.

# Prerequisites
To install all the dependencies, docker engine must be installed on the end-users' device. Please refer the [user manual](https://docs.docker.com/engine/install/ubuntu) for Ubuntu. Please install the docker engine corressponding to your active distro/version.

### Dependencies
All the dependencies required for the successfull working of the Motifizer source code is included with the [Dockerfile](https://github.com/abhikbhattacharjee/Motifizer/Blob/master/Dockerfile) provided with the source code.
Major Dependencies include:
- Python 3.6
- MEME Suite (Version : 5.0.4)
- Bedtools (Version : 2.27.1)
- Hisat2 (Version : 2.1.0)
- Samtools (Version : 1.9)
- EdgeR (Version : 3.20.2)
- Homer
- Flask (Version : 1.1.2)
- TensorFlow (Version : 2.1.0)
- Keras (Version : 2.3.1)
- Scikit-learn (Version : 0.20.4)

# Installation
The successfull implementation is guranteed on any computer system running a Linux Operating System. 

Clone the GitHub repository in the directory of your liking. Please note that **minimum availabe space should be atleast 4.8 GB**.

### Building the Docker container
Traverse into the directory location where the Git repo is cloned and enter the following command via command line interface:
```bash
docker build --tag motifizer .
```
This process requires an active internet connection.

To ensure the successfull build of the docker container, execute the following command via command line interface:
```bash
docker images
```

It should show a similar output:
```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
motifizer           latest              a7f8881f70ee        5 hours ago         4.82GB
ubuntu              18.04               c3c304cb4f22        6 weeks ago         64.2MB
debian              testing             4d9505b13e32        6 weeks ago         118MB
```

### To run the docker container
After the successfull build of the docker container, execute the following bash command to run the modules mentioned above for your own dataset:
```bash
docker run -i -t -p 5000:5000 motifizer
```

To **add your own data into the docker container** in order to carry out various processes and analysis, follow the given [link](https://docs.docker.com/engine/reference/commandline/cp) from the docker documentation.

# Accessing the GUI for Motifizer
To access the web-based GUI on your localhost, type in the following command while inside the docker container:
```bash
python bookmanager.py
```
On successfull execution, the following output should be visible on the command line:
```
motifizer@c3c7c64aaa9f:~$ python bookmanager.py
 * Serving Flask app "bookmanager" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 280-051-235
 ```
 **Right-click on the IP address** mentioned in the message and open the link in order to access the web-based GUI.
 - **Please note that all the fields mentioned in the Web GUI are compulsory. Omission of any one field would result in unsuccessfull execution of the module**
 
 In order to close the GUI, close the browser tab and press **CTRL+C** on the terminal to close the flask application deamon.
 
 
 # Accessing the CLI Version of Motifizer
 The various commands required to execute the codes via command-line are as follows:
 
 ### For Analysis Module
 ```bash
 ./BE_Project.sh <JASPAR_file_or_equivalent> <RNA_Seq_data_Excel> <sheet_name_for_UP_regulation_data> <sheet_name_for_DOWN_regulation_data> <sheet_name_for_NOTDIFF_regulation_data> <dmel_genome> <genome_fa_file> <extra_bases> <File_Up> <File_Down> <File_Notdiff> <Save_results>
 ```
