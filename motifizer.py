import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from flask import Flask
from flask import render_template
from flask import request
import os
from os.path import exists

def get_shell_script_output_using_communicate(k):
    session = subprocess.Popen(["./analysis.sh" + k])
    stdout, stderr = session.communicate()
    if stderr:
        raise Exception("Error "+str(stderr))
    return stdout.decode('utf-8')

def get_shell_script_output_using_check_output(k,l,m,n,o,p,q,r,s,t,u,v):
    stdout = check_output(['./analysis.sh',k,l,m,n,o,p,q,r,s,t,u,v]).decode('utf-8')
    return stdout

def get_shell_script_output_using_check_output1(a,b,c,d,e):
    stdout = check_output(['./ChIP_seq.sh',a,b,c,d,e]).decode('utf-8')
    return stdout
    
def get_shell_script_output_using_check_output2(a,b,c,d,e,f,g,h):
	stdout = check_output(['./predict.sh',a,b,c,d,e,f,g,h]).decode('utf-8')
	return stdout	
	
def get_shell_script_output_using_check_output3(a,b,c,d,e,f):
	stdout = check_output(['./rna_hisat_pe.sh',a,b,c,d,e,f]).decode('utf-8')
	return stdout	

def get_shell_script_output_using_check_output4(a,b,c,d,e,f,g):
	stdout = check_output(['./edgeR_rna_seq.sh',a,b,c,d,e,f,g]).decode('utf-8')
	return stdout

def get_shell_script_output_using_check_output5(a,b,c,d,e):
	stdout = check_output(['./chip_annotation.sh',a,b,c,d,e]).decode('utf-8')
	return stdout	

def get_shell_script_output_using_check_output6(a,b,c,d,e):
	stdout = check_output(['./rna_hisat_se.sh',a,b,c,d,e]).decode('utf-8')
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
    return render_template("rna_seq_home.html")

@app.route('/edger',methods=['GET','POST'])
def test7():
    #get_shell_script_output_using_communicate()
    return render_template("rna_edgeR.html")

@app.route('/chip_home',methods=['GET','POST'])
def test8():
    #get_shell_script_output_using_communicate()
    return render_template("chip_home.html")

@app.route('/chip_annotate',methods=['GET','POST'])
def test10():
    #get_shell_script_output_using_communicate()
    return render_template("chip_annotate_pg.html")
    
@app.route('/rna_seq_se',methods=['GET','POST'])
def test11():
    #get_shell_script_output_using_communicate()
    return render_template("run_hisat_single_end.html")

@app.route('/rna_seq_pe',methods=['GET','POST'])
def test12():
    #get_shell_script_output_using_communicate()
    return render_template("rna_hisat.html")

@app.route('/run',methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		print("Uploading files, please wait")
		f1 = request.files['jaspar_path']
		f1.save(f1.filename)
		f2 = request.files['rna_path']
		f2.save(f2.filename)
		f3 = request.files['dmel']
		f3.save(f3.filename)
		f4 = request.files['genome']
		f4.save(f4.filename)
	
		jaspar_path1 = f1.filename  # access the data inside 
		rna_path1 = f2.filename
		up_path1 = request.form.get('up_data')
		down_path1 = request.form.get('down_data')
		not_path1 = request.form.get('not_data')
		dmel_path1 = f3.filename
		genome_path1 = f4.filename
		base_pair_path1 = request.form.get('basepairs')
		up_name_path1 = request.form.get('up_seq')
		down_name_path1 = request.form.get('down_seq')
		not_name_path1 = request.form.get('not_seq')
		save_path1 = request.form.get('save_res')	
    	
	get_shell_script_output_using_check_output(str(jaspar_path1),str(rna_path1),str(up_path1),str(down_path1),str(not_path1),str(dmel_path1),str(genome_path1),str(base_pair_path1),str(up_name_path1),str(down_name_path1),str(not_name_path1),str(save_path1))
    #get_shell_script_output_using_communicate()
	return render_template("index.html")

@app.route('/run_chip',methods=['GET', 'POST'])
def home1():
	if request.method == 'POST':
		print("Uploading files, please wait")
		f1 = request.files['genome_path']
		f1.save(f1.filename)
		f2 = request.files['test_fq']
		f2.save(f2.filename)
		f3 = request.files['input_fq']
		f3.save(f3.filename)
		f4 = request.files['gtf']
		f4.save(f4.filename)
		genome_path2 = f1.filename  # access the data inside 
		test_fq_path1 = f2.filename
		input_fq_path1 = f3.filename
		genome_name1 = f4.filename
		save_path2 = request.form.get('save_results')	
    	
	get_shell_script_output_using_check_output1(str(genome_path2),str(test_fq_path1),str(input_fq_path1),str(genome_name1),str(save_path2))
    #get_shell_script_output_using_communicate()
	return render_template("chip_module.html")

@app.route('/run_pred',methods=['GET','POST'])
def pred_home():
	if request.method == 'POST':
		print("Uploading files, please wait")
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
		print("Uploading files, please wait")
		f1 = request.files['genome_path_rna']
		f1.save(f1.filename)
		f2 = request.files['fq1']
		f2.save(f2.filename)
		f3 = request.files['fq2']
		f3.save(f3.filename)
		f4 = request.files['gtf_path']
		f4.save(f4.filename)	
		
		genome_fa_rna = f1.filename
		fq1 = f2.filename
		fq2 = f3.filename
		gtf_path = f4.filename
		htseq_name = request.form.get('htseq_name')
		save_res_rna = request.form.get('save_results_rna')
		
	get_shell_script_output_using_check_output3(str(genome_fa_rna),str(fq1),str(fq2),str(gtf_path),str(htseq_name),str(save_res_rna))
	return render_template("rna_module.html")

@app.route('/run_hisat_se',methods=['GET','POST'])
def rna_hisat_se():
	if request.method == 'POST':
		print("Uploading files, please wait")
		f1 = request.files['genome_path_rna_se']
		f1.save(f1.filename)
		f2 = request.files['fq_se']
		f2.save(f2.filename)
		#f3 = request.files['fq2']
		#f3.save(f3.filename)
		f4 = request.files['gtf_path_se']
		f4.save(f4.filename)	
		
		genome_path_rna_se = f1.filename
		fq_se = f2.filename
		#fq2 = f3.filename
		gtf_path_se = f4.filename
		htseq_name_se = request.form.get('htseq_name_se')
		save_results_rna_se = request.form.get('save_results_rna_se')
	get_shell_script_output_using_check_output6(str(genome_path_rna_se),str(fq_se),str(gtf_path_se),str(htseq_name_se),str(save_results_rna_se))
	return render_template("run_hisat_single_end.html")

@app.route('/run_edgeR',methods=['GET','POST'])
def rna_home_edgeR():
	if request.method == 'POST':
		print("Uploading files, please wait")
		f1 = request.files['ptf1']
		f1.save(f1.filename)
		f2 = request.files['ptf2']
		f2.save(f2.filename)
		f3 = request.files['ptf3']
		f3.save(f3.filename)
		f4 = request.files['pcf1']
		f4.save(f4.filename)
		f5 = request.files['pcf2']
		f5.save(f5.filename)
		f6 = request.files['pcf3']
		f6.save(f6.filename)
		
		test1 = f1.filename
		test2 = f2.filename
		test3 = f3.filename
		control1 = f4.filename
		control2 = f5.filename
		control3 = f6.filename
		save_res_rna_edgeR = request.form.get('save_results_rna_edgeR')
		
	get_shell_script_output_using_check_output4(str(test1),str(test2),str(test3),str(control1),str(control2),str(control3),str(save_res_rna_edgeR))
	return render_template("rna_module.html")


@app.route('/run_chip_annotate',methods=['GET','POST'])
def chip_annotate():
	if request.method == 'POST':
		print("Uploading files, please wait")
		f1 = request.files['bam_ip_motifizer']
		f1.save(f1.filename)
		f2 = request.files['test_BAM_motifizer']
		f2.save(f2.filename)
		f3 = request.files['filtered_GTF2_motifizer']
		f3.save(f3.filename)
		f4 = request.files['gen_fa_chip_ann']
		f4.save(f4.filename)
		annotate_bam = f1.filename
		annotate_test = f2.filename
		annotate_gtf = f3.filename
		gen_fa_annotate = f4.filename
		annotate_save_res = request.form.get('save_results_chip2')
		
	get_shell_script_output_using_check_output5(str(annotate_bam),str(annotate_test),str(annotate_gtf),str(annotate_save_res),str(gen_fa_annotate))
	return render_template("chip_annotate_pg.html")


#app.run(debug=True)

if __name__ == "__main__": 
	app.run(debug=True,host = '0.0.0.0', port = 5000)
