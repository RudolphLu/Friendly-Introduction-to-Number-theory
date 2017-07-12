# Find the L(n),T(n)
#

main_array = []

def search_match(s1,max_length):
    i=0
    match = -1
    if(max_length==0):
        return -1
    while i<max_length:
        #print ('search_match ...',main_array[s1],main_array[s1-max_length+i],max_length)
        if main_array[s1+i] == main_array[s1-max_length+i]:		    
            match = 1
        else:
            match = -1
            return search_match(s1,max_length-1)
        i = i+1
    return match

def TripleNAddOne(a,step,insert_position,compare_position):
    new_a = 0
    if(a%2 == 1):
        new_a = 3*a + 1
    else:
        new_a = a/2        
    main_array.append(new_a)	
    step += 1
    #Length of compare is insert_position-compare_position
    if(insert_position>=compare_position):
        cmp_length = insert_position-compare_position+1
    else:
	    cmp_length = 0

    if(cmp_length>compare_position):
        compare_position += 1
        return TripleNAddOne(new_a,step,insert_position,compare_position)
    if(insert_position>=compare_position):
        #print ('TripleNAddOne ...',insert_position,compare_position)		
        rlt = search_match(compare_position,cmp_length)
        if(rlt!=-1):
            return (main_array[compare_position-1],compare_position)
    insert_position += 1
    return TripleNAddOne(new_a,step,insert_position,compare_position)

	
for n in range (1,100):
    main_array = [n]
    return_list = TripleNAddOne(n,0,0,2)
    print ('Result','[',n,']',return_list)