import subprocess

correct_output = "0.9384758934759384\n"   # this is a test value

def test_run():
    p = subprocess.Popen('python gc-of-seqs.py single_input.fastq', shell=True, stdout=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    assert stdout == correct_output