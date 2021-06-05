def solution(cords):
    cords = set(cords)
    final_cords = set()

    selection_box = set()
    insert = False
    deletion = False
    for x in range(max_x+1):

        for ele in cords:        
            if ele[0] == x:
                selection_box.add(ele)
                insert = True

            if ele[1] == x:
                deletion = True  
                
        if insert:
            
            max_ht = max([i[2] for i in selection_box])

            final_cords.add(([(i[0],i[2]) for i in selection_box if i[2]==max_ht])[0])           


            insert =False

        if deletion:
            

            if len(set([i[2] for i in selection_box]))>1:
                
                dele_ele = max([j[2] for j in selection_box if j[1]==x])
                selection_box = set([j for j in selection_box if j[1]!=x])
                
                max_ht = max([i[2] for i in selection_box])
                
                if(dele_ele>max_ht):
                    final_cords.add((x,max_ht))

            else:
                final_cords.add((x,0)) 
                selection_box = set([j for j in selection_box if j[1]!=x])

            

            deletion= False


    return final_cords
