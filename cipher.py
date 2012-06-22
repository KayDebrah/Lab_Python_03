#Part II Secret Messages
#Question 1
phrase=raw_input("Enter sentence to encrypt: ")
shift=int(raw_input("Enter shift value: "))

encoded_phrase=''

for c in phrase:
    encoded_phrase=encoded_phrase+c
    print encoded_phrase
#
    

#Question 2
phrase=raw_input("Enter sentence to encrypt: ")
shift=int(raw_input("Enter shift value: "))

length=len(phrase)

encoded_phrase='x'

for c in phrase:
    ascii_code=ord(c)
    if(ascii_code==32):
        code=int((ascii_code)+shift)%6
        ltr_rvs=chr(code)
        ltr='x'
        ltr=ltr+' '
        encoded_phrase=ltr
    elif(ascii_code==33):
        code=int((ascii_code)+shift)%6
        ltr_rvs=chr(code)
        ltr='x'
        ltr=ltr+'!'
        encoded_phrase=ltr
    else:
        code=int((ascii_code)+shift)%6
        ltr_rvs=chr(code)
        ltr='x'
        ltr+=ltr
    
    print encoded_phrase,
print "\n"

    #'with shift: ',code,'new cipher:',ltr_rvs
#  

#Question 3
phrase=raw_input("Enter sentence to encrypt: ")
shift=int(raw_input("Enter shift value: "))

length=len(phrase)

encoded_phrase=''
print "Encoded phrase: "
for c in phrase:
    ascii_code=ord(c)
    if(ascii_code>=65 and ascii_code<122):
                  
        code=int(ascii_code)+shift
        if(code>=91 and code<97):
            remainder=code-90
            ltr_rvs=chr(65+(remainder-1))
            print ltr_rvs,
        elif (code>=123 and code<128):
            remainder=code-122
            ltr_rvs=chr(97+(remainder-1))
            print ltr_rvs,
            
        else:
            ltr_rvs=chr(code)
            print  ltr_rvs,
    elif (ascii_code>=32 and ascii_code<48):
        ltr_rvs=c
        print ltr_rvs,
    else:
        code=int((ascii_code)+shift)%6
        #ascii_code=ord(code)
        ltr_rvs=chr(ascii_code)
        print code

        #'with shift: ',code,'new cipher:',ltr_rvs
#
            
