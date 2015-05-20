def create_master_turnstile_file(filenames, output_file):
    with open(output_file, 'w') as master_file:
       master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
       for filename in filenames:
           f_in = open(filename, 'r')
           master_file.write(f_in.read())
           f_in.close()
       master_file.close()
