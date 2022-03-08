from dataclasses import replace


print('''   _____       .___.__   __   .__  
  /  _  \    __| _/|__|_/  |_ |__| 
 /  /_\  \  / __ | |  |\   __\|  | 
/    |    \/ /_/ | |  | |  |  |  | 
\____|__  /\____ | |__| |__|  |__| 
        \/      \/                 
                                   ''')
with open("website.log.txt","r") as f:
                              lines=f.readlines()
                              with open("output.txt",'wt') as nf:
                                  for line in lines:
                                                line=line.split(" ")
                                                nf.write("Ip \t datetime \t time zone \t request type \t path \t http protocol \t staus code \t packet size \t user agent \n ")
                                                nf.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(str(line[0]).replace('"',' '),line[3],line[5],line[6],line[7],line[8],line[9],line[11]))
    
    