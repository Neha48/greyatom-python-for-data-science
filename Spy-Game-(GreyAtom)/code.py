# --------------
#Code starts here

#Function to read file
def read_file(path):
    with open(path,'r') as fie:
    #Opening of the file located in the path in 'read' mode
        sentence=(list)(fie)[0]
    #Reading of the first line of the file and storing it in a variable
    fie.close()
    #Closing of the file
    return sentence
    #Returning the first line of the file
#Calling the function to read file
sample_message= read_file(file_path)
print(sample_message)
#Printing the line of the file
#Function to fuse message
def fuse_msg(message_a,message_b):
    quotient=int(message_b)//int(message_a)
    #Integer division of two numbers
    return str(quotient)
    #Returning the quotient in string format

message_1=read_file(file_path_1)
message_2=read_file(file_path_2)
print(message_1)
print(message_2)
#Calling the function to read file 
#Calling the function to read file
#Calling the function 'fuse_msg'
 
secret_msg_1=fuse_msg(message_1,message_2)
print(secret_msg_1)
#Printing the secret message 
#Function to substitute the message
def substitute_msg(message_c):
    sub=''
    if message_c =='Red':
        sub='Army General'
    elif message_c=='Green':
        sub='Data Scientist'
    elif message_c =='Blue':
        sub='Marine Biologist'
    #If-else to compare the contents of the file
    return sub
    
    #Returning the substitute of the message

message_3=read_file(file_path_3)
print(message_3)
#Calling the function to read file
secret_msg_2= substitute_msg(message_3)

#Calling the function 'substitute_msg'
print(secret_msg_2)
#Printing the secret message

#Function to compare message
def compare_msg(message_d,message_e):
    a_list=message_d.split()
    #Splitting the message into a list
    b_list=message_e.split()
    c_list=[x for x in a_list if x not in b_list]
    #Splitting the message into a list
    final_msg=' '.join(c_list)
    return final_msg
    #Comparing the elements from both the lists
    #Combining the words of a list back to a single string sentence
    
    #Returning the sentence

message_4=read_file(file_path_4)
message_5=read_file(file_path_5)
#Calling the function to read file
#Calling the function to read file
#Calling the function 'compare messages'

secret_msg_3=compare_msg(message_4,message_5)
#Printing the secret message
print(secret_msg_3)
#Function to filter message
def extract_msg(message_f):
    a_list=message_f.split()    
    #Splitting the message into a list
    even_word=lambda x:len(x)%2==0
    b_list=list(filter(even_word,a_list))
    #Creating the lambda function to identify even length words
    final_msg = ' '.join(b_list)
    return final_msg
    #Splitting the message into a list
    
    #Combining the words of a list back to a single string sentence
    
    #Returning the sentence
message_6=read_file(file_path_6)
print(message_6)
#Calling the function to read file
secret_msg_4=extract_msg(message_6)
print(secret_msg_4)
#Calling the function 'filter_msg'

#Printing the secret message
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
secret_msg=' '.join(message_parts)

# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message

#Function to write inside a file
def write_file(secret_msg,path):
    f=open(path,'a+')
    #Opening a file named 'secret_message' in 'write' mode
    f.write(secret_msg)
    f.close()
    #Writing to the file
    #Closing the file
#Calling the function to write inside the file    
write_file(secret_msg,final_path)
#Printing the entire secret message
print(secret_msg)
#Code ends here


