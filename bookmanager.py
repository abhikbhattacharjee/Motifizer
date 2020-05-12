import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from flask import Flask
from flask import render_template
from flask import request
import os

def get_shell_script_output_using_communicate(k):
    session = subprocess.Popen(["./BE_Project.sh" + k])
    stdout, stderr = session.communicate()
    if stderr:
        raise Exception("Error "+str(stderr))
    return stdout.decode('utf-8')

def get_shell_script_output_using_check_output(k,l,m,n,o,p,q,r,s,t,u,v):
    stdout = check_output(['./BE_Project.sh',k,l,m,n,o,p,q,r,s,t,u,v]).decode('utf-8')
    return stdout

def get_shell_script_output_using_check_output1(a,b,c,d,e):
    stdout = check_output(['./ChIP_seq.sh',a,b,c,d,e]).decode('utf-8')
    return stdout
    
def get_shell_script_output_using_check_output2(a,b,c,d,e,f,g,h):
	stdout = check_output(['./predict.sh',a,b,c,d,e,f,g,h]).decode('utf-8')
	return stdout	
	
def get_shell_script_output_using_check_output3(a,b,c,d,e,f,g,h,i):
	stdout = check_output(['./RNA_seq.sh',a,b,c,d,e,f,g,h,i]).decode('utf-8')
	return stdout	

def get_shell_script_output_using_check_output4(a,b,c,d,e,f,g):
	stdout = check_output(['./edgeR_rna_seq.sh',a,b,c,d,e,f,g]).decode('utf-8')
	return stdout	
	
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def test1():
    #get_shell_script_output_using_communicate()
    return render_template("ref_page.html")

@app.route('/analysis',methods=['GET','POST'])
def test2():
    #get_shell_script_output_using_communicate()
    return render_template("index.html")

@app.route('/chip_seq',methods=['GET','POST'])
def test3():
    #get_shell_script_output_using_communicate()
    return render_template("chip_module.html")
    
@app.route('/prediction',methods=['GET','POST'])
def test4():
    #get_shell_script_output_using_communicate()
    return render_template("prediction_module.html")

@app.route('/rna_seq',methods=['GET','POST'])
def test5():
    #get_shell_script_output_using_communicate()
    return render_template("rna_module.html")

@app.route('/hisat',methods=['GET','POST'])
def test6():
    #get_shell_script_output_using_communicate()
    return render_template("rna_hisat.html")

@app.route('/edger',methods=['GET','POST'])
def test7():
    #get_shell_script_output_using_communicate()
    return render_template("rna_edgeR.html")

@app.route('/run',methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		jaspar_path1 = request.form.get('jaspar_path')  # access the data inside 
		rna_path1 = request.form.get('rna_path')
		up_path1 = request.form.get('up_data')
		down_path1 = request.form.get('down_data')
		not_path1 = request.form.get('not_data')
		dmel_path1 = request.form.get('dmel')
		genome_path1 = request.form.get('genome')
		base_pair_path1 = request.form.get('basepairs')
		up_name_path1 = request.form.get('up_seq')
		down_name_path1 = request.form.get('down_seq')
		not_name_path1 = request.form.get('not_seq')
		save_path1 = request.form.get('save_res')	
    	
	get_shell_script_output_using_check_output(str(jaspar_path1),str(rna_path1),str(up_path1),str(down_path1),str(not_path1),str(dmel_path1),str(genome_path1),str(base_pair_path1),str(up_name_path1),str(down_name_path1),str(not_name_path1),str(save_path1))
    #get_shell_script_output_using_communicate()
	return render_template("index.html")

@app.route('/run1',methods=['GET', 'POST'])
def home1():
	if request.method == 'POST':
		genome_path2 = request.form.get('genome_path')  # access the data inside 
		test_fq_path1 = request.form.get('test_fq')
		input_fq_path1 = request.form.get('input_fq')
		genome_name1 = request.form.get('genome_name')
		save_path2 = request.form.get('save_results')	
    	
	get_shell_script_output_using_check_output1(str(genome_path2),str(test_fq_path1),str(input_fq_path1),str(genome_name1),str(save_path2))
    #get_shell_script_output_using_communicate()
	return render_template("chip_module.html")

@app.route('/run_pred',methods=['GET','POST'])
def pred_home():
	if request.method == 'POST':
		jaspar_path_pred1 = request.form.get('jaspar_path_pred')
		chip_pred_data = request.form.get('chip_pred')
		pred_sheet = request.form.get('sheet_pred')
		pred_dmel = request.form.get('dmel_pred')
		pred_genome = request.form.get('genome_pred')
		base_pred = request.form.get('basepairs_pred')
		pred_seq = request.form.get('seq_pred')
		pred_save = request.form.get('save_res_pred')
		
	get_shell_script_output_using_check_output2(str(jaspar_path_pred1),str(chip_pred_data),str(pred_sheet),str(pred_dmel),str(pred_genome),str(base_pred),str(pred_seq),str(pred_save))
	return render_template("prediction_module.html")

@app.route('/run_hisat',methods=['GET','POST'])
def rna_home():
	if request.method == 'POST':
		genome_fa_rna = request.form.get('genome_path_rna')
		fq1 = request.form.get('fq1')
		fq2 = request.form.get('fq2')
		sam = request.form.get('sam_name')
		bam = request.form.get('bam_name')
		fbam = request.form.get('fbam_name')
		gtf_path = request.form.get('gtf_path')
		htseq_name = request.form.get('htseq_name')
		save_res_rna = request.form.get('save_results_rna')
		
	get_shell_script_output_using_check_output3(str(genome_fa_rna),str(fq1),str(fq2),str(sam),str(bam),str(fbam),str(gtf_path),str(htseq_name),str(save_res_rna))
	return render_template("rna_module.html")

@app.route('/run_edgeR',methods=['GET','POST'])
def rna_home_edgeR():
	if request.method == 'POST':
		test1 = request.form.get('ptf1')
		test2 = request.form.get('ptf2')
		test3 = request.form.get('ptf3')
		control1 = request.form.get('pcf1')
		control2 = request.form.get('pcf2')
		control3 = request.form.get('pcf3')
		save_res_rna_edgeR = request.form.get('save_results_rna_edgeR')
		
	get_shell_script_output_using_check_output4(str(test1),str(test2),str(test3),str(control1),str(control2),str(control3),str(save_res_rna_edgeR))
	return render_template("rna_module.html")


app.run(debug=True)
