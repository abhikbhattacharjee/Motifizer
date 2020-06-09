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
- <JASPAR_file_or_equivalent> - Path to/ Name of JASPAR or equivalent database
- <RNA_Seq_data_excel> - Path/File name for the RNA-Seq Data which is to be parsed into the analysis module
- <sheet_name_for_UP_regulation_data> - Sheet name where UP regulated sequences are stored
- <sheet_name_for_DOWN_regulation_data> - Sheet name where DOWN regulated sequences are stored
- <sheet_name_for_NOTDIFF_regulation_data> - Sheet name where NOT DIFFERENTIALLY regulated sequences are stored
- <dmel_genome> - Path to dmel genome file
- <genome_fa_file> - Path to genome fasta file
- <extra_bases> - Extra bases to be added to the sequences
- <File_Up> - File name to store UP regulated sequences
- <File_Down> - File name to store DOWN regulated sequences 
- <File_Notdiff> - File name to store NOT DIFFERENTIALLY regulated sequences
- <Save_results> - Path to save results/Directory name to be created

### For ChIP_Seq Module
```bash
./ChIP_seq.sh <path_genome_fa> <path_test_fq> <path_input_fq> <genome_name> <save_res>
```

- <path_genome_fa> - Path to the genome fasta file 
- <path_test_fq> - Path to the test FASTQ file (.gzip)
- <path_input_fq> - Path to the input FASTQ file (.gzip)
- <genome_name> - Genome name (dm6,etc)
- <save_res> - Path to save results/Directory name to be created

### For RNA-Seq Module
#### HISAT2 Analysis
```bash
./RNA_seq.sh <genome_fa> <fq1_file> <fq2_file> <sam_file> <bam_file> <filtered_bam> <gene_gtf> <htseq_file> <save_res>
```

- <genome_fa> - Path to genome file for which indexing is to be done
- <fq1_file> - Path to first FASTQ file
- <fq2_file> - Path to second FASTQ file
- <sam_file> - Name of SAM file to be created
- <bam_file> - Name of BAM file to be created
- <filtered_bam> - Name of Filtered BAM file to be created
- <gene_gtf> - Path to gene gtf file
- <htseq_file> - Desired HTSEQ file name
- <save_res> - Path to save results/Directory name to be created

#### EdgeR Analysis
```bash
./edgeR_rna_seq.sh <test_file_1> <test_file_2> <test_file_3> <control_file_1> <control_file_2> <control_file_3> <save_res> 
```

- <test_file_1> - Path to test file 1
- <test_file_2> - Path to test file 2
- <test_file_3> - Path to test file 3
- <control_file_1> - Path to control file 1
- <control_file_2> - Path to control file 2
- <control_file_3> - Path to control file 3
- <save_res> - Path to save results/Directory name to be created

### For Prediction Module
```bash
./predict.sh <JASPAR_file_or_equivalent> <ChIP_Seq_data_Excel> <sheet_name_for_pred_data> <dmel_genome> <genome_fa_file> <extra_bases> <File_Pred> <Save_results>
```

- <JASPAR_file_or_equivalent> - Path to/ Name of JASPAR or equivalent database
- <RNA_Seq_data_excel> - Path/File name for the RNA-Seq Data which is to be parsed into the analysis module
- <sheet_name_for_pred_data> - Sheet name where Predicted sequences are to be stored
- <dmel_genome> - Path to dmel genome file
- <genome_fa_file> - Path to genome fasta file
- <extra_bases> - Extra bases to be added to the sequences
- <File_Pred> - File name to store Predicted sequences
- <Save_results> - Path to save results/Directory name to be created

# Additional Information
To get more information about the implementation details, tools and technologies used, design features, etc. please refer to the following [Project Report](https://drive.google.com/file/d/1mfGzS_NLxhY2437P36VQkCamRnRx_TTu/view?usp=sharing). 

This code is licensed under MIT License and its associated conditions must be followed if you wish to include it in your projects/research.
