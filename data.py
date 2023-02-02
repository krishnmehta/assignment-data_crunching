import pandas as pd


#Reading the tsv file using pandas
file1 = pd.read_csv('user_email_hash.1m.tsv',sep='\t')
file2 = pd.read_csv('ip_1m.tsv',sep='\t')
file3 = pd.read_csv('plain_32m.tsv',sep='\t')

# print(file1.head(5))

#Adding columns in dictionary
output_dict = {'Id':file1['id'],
               'username': file1['username'],
               'email': file1['email'],
               'hashed_password': file1['password'],
               'plaintext_password': file3.iloc[:,1], #Here iloc has been used since there is no column names given in plain_32m.tsv
               'ip': file2['ip_address']}


#Convert Dictionary using DataFrame
dFrame = pd.DataFrame(output_dict)
#print(dFrame.head(5))


# Exporting TSV files
dFrame.to_csv('Output_file.tsv', sep="\t") #\t is used to export it in TSV format

