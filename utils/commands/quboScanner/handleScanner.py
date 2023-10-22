import subprocess
def scan(quboCMD):
    results =  subprocess.run(quboCMD, shell=True, capture_output=True)
    print(results.stdout.decode())
    


scan('java -Dfile.encoding=UTF-8 -jar qubo.jar -port 2000-20001 -th 5000 -ti 100 -range 127.0.0.1')