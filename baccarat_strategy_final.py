#!/usr/bin/python
#


import numpy as np

import random

"""get canvas"""
def get_canvas():
    
    temp_decks= generate_deck(8)
    temp_canvas=np.zeros([20,80])
    temp_count=0
    while len(temp_decks)>10:


        test_result=simulate_game(temp_decks)
        if test_result!= 0:
            temp_result=test_result


        if temp_count==0:
            temp_canvas[0,0]=temp_result

            pre_col=0
            pre_row=0
            temp_count+=1


        else:
            if previous== temp_result:

                pre_row+=1
                temp_canvas[pre_row,pre_col]=temp_result

            else:
                pre_col+=1
                pre_row=0
                temp_canvas[pre_row,pre_col] = temp_result
        previous= temp_result
    return temp_canvas
    
"""find_col_row"""
def find_col_row(canvas):
    
    for col in xrange(np.shape(canvas)[1]):
        if np.sum(canvas[:,col])==0:
            col_ret=col-1
            break
          
            
    for row in xrange(np.shape(canvas)[0]):
        if canvas[row, col_ret]==0:
            row_ret=row-1
            break
    return (row_ret, col_ret)

"""stratgey"""
def strategy(canvas,threshold):
    
    temp_stratgey=None
    
    temp_most_left= sy_vision(canvas,threshold)
    
    temp_most_right= find_col_row(canvas)[1]
    
    temp_row= find_col_row(canvas)[0]
    
    #canvas[:,temp_most_left:temp_most_right+1]
    
    if  cmp_joint_num(canvas[:,temp_most_left:temp_most_right+1]) >= threshold:
        if cmp_joint_num(canvas[:,temp_most_left])== cmp_joint_num(canvas[:,temp_most_right]):
            temp_stratgey='same'
        else:
            temp_stratgey='oppsite'
    else:
        return 0
    #return temp_stratgey,       
    if canvas[temp_row, temp_most_right]==1:
        if temp_stratgey=='same':
            return 1
        else:
            return 2
    if canvas[temp_row, temp_most_right]==2:
        if temp_stratgey=='same':
            return 2
        else:
            return 1
"""cmp_joint_num"""
def cmp_joint_num(canvas):
    temp_canvas= np.copy(canvas)
    index_= temp_canvas==2
    temp_canvas[index_]=1
    return np.sum(temp_canvas)
"""simulate_bets"""
def simulate_bets(threshold,bar):
    temp_decks= generate_deck(8)
    temp_canvas=np.zeros([20,80])
    temp_count=0
    money=0
    bets=0
    
    while len(temp_decks)>25:

        cont=True
        comp=False
        if cmp_joint_num(temp_canvas)>=threshold:

            if sy_vision(temp_canvas,threshold,bar) !=0:
                next_move= strategy(temp_canvas,threshold)

                comp=True
        while cont:
            test_result=simulate_game(temp_decks)
            if test_result!= 0:
                temp_result=test_result
                cont= False
        if comp:
            #print temp_canvas
            #print find_col_row(temp_canvas)
            #print '------------------------'
            if next_move==temp_result:
                money+=1

            bets+=1




        if test_result!= 0:
            temp_result=test_result


        if temp_count==0:
            temp_canvas[0,0]=temp_result

            pre_col=0
            pre_row=0
            temp_count+=1


        else:
            if previous== temp_result:

                pre_row+=1
                temp_canvas[pre_row,pre_col]=temp_result

            else:
                pre_col+=1
                pre_row=0
                temp_canvas[pre_row,pre_col] = temp_result

        previous= temp_result
    return money, bets,temp_canvas
"""sy_vision"""
def sy_vision(canvas,threshold,bar=3):
    temp_tuple= find_col_row(canvas)
    temp_row=temp_tuple[0]
    temp_col=temp_tuple[1]
    key=0
    find_the_best=False
    
    for most_left in range(temp_col-1,-1,-1):
        screen_canvas= canvas[:,most_left:]
        
        if (temp_col-most_left)%2!=0:
            """ even sy"""
            for i in xrange((temp_col - most_left +1)/2):
                """ most left and most rigth checking"""
                
                if i ==0:
                    condition_even= ((cmp_joint_num(screen_canvas[:,i])-cmp_joint_num(screen_canvas[:,temp_col-most_left]))<=1)
                    if np.all(screen_canvas[:temp_row+1,i]== screen_canvas[:temp_row+1, temp_col-most_left]) and condition_even:
                        #print 'even_most_checking_PASS'
                        pass
                    else:
                        #print 'even_most_checking_BREAK'
                        break
                        
                #middle checking
                
                else:
                    if np.all(screen_canvas[:,i]== screen_canvas[:, temp_col-most_left-i]):
                        pass 
                        if i == (temp_col-most_left-1)/2:
                            find_the_best=True
                            key=most_left
                            #print 'got_it_____EVEN'
                            break
                    else:
                        break
                        #print #'middle_checking______BREAK'
                        
        if (temp_col - most_left)%2==0:
            """ odd sy"""
            for i in xrange((temp_col-most_left)/2+1):
                condition_odd= ((cmp_joint_num(screen_canvas[:,i])-cmp_joint_num(screen_canvas[:,temp_col-most_left]))<=1)
                if i==0:
                    if np.all(screen_canvas[:temp_row+1, i] == screen_canvas[:temp_row+1,temp_col-most_left ]) and condition_odd:
                        pass
                        #print 'odd_most____pass' 
                    else:
                        #print 'odd_most_break'
                        break
                """ middle checking """
                if i !=0 and i != (temp_col-most_left)/2:
                    if np.all(screen_canvas[:,i]==screen_canvas[:,temp_col-most_left-i]):
                        pass
                        #print 'odd_middle_pass' 
                    else:
                        #print  'odd_middle_break'
                        break
                if i== (temp_col-most_left)/2:
                    key= most_left
                    find_the_best=True
                    #print 'odd_got_it'
                    break
                    
                    
                        
                        
        if find_the_best:
            if cmp_joint_num(canvas[:,most_left:temp_col])>= threshold and cmp_joint_num(canvas[:,temp_col])>=bar:
                #print 'got it'
                break
            else:
                find_the_best=False
                key=0
            
    return key
            
"""sy_vision_print"""
def sy_vision_print(canvas,threshold):
    temp_tuple= find_col_row(canvas)
    temp_row=temp_tuple[0]
    temp_col=temp_tuple[1]
    key=0
    find_the_best=False
    check_num=True
    
    for most_left in range(temp_col-1,-1,-1):
        screen_canvas= canvas[:,most_left:]
        
        if (temp_col-most_left)%2!=0:
            """ even sy"""
            for i in xrange((temp_col - most_left +1)/2):
                """ most left and most rigth checking"""
                
                if i ==0:
                    condition_even= ((cmp_joint_num(screen_canvas[:,i])-cmp_joint_num(screen_canvas[:,temp_col-most_left]))<=1)
                    if np.all(screen_canvas[:temp_row+1,i]== screen_canvas[:temp_row+1, temp_col-most_left]) and condition_even:
                        print 'even_most_checking_PASS'
                        pass
                    else:
                        print 'even_most_checking_BREAK'
                        break
                        
                #middle checking
                
                else:
                    if np.all(screen_canvas[:,i]== screen_canvas[:, temp_col-most_left-i]):
                        pass 
                        if i == (temp_col-most_left-1)/2:
                            find_the_best=True
                            key=most_left
                            print 'got_it_____EVEN'
                            break
                    else:
                        print 'middle_checking______BREAK'
                        
        if (temp_col - most_left)%2==0:
            """ odd sy"""
            for i in xrange((temp_col-most_left)/2+1):
                condition_odd= ((cmp_joint_num(screen_canvas[:,i])-cmp_joint_num(screen_canvas[:,temp_col-most_left]))<=1)
                print condition_odd
                
                print cmp_joint_num(screen_canvas[:,i])
                print cmp_joint_num(screen_canvas[:,temp_col-most_left])
                if i==0:
                    if np.all(screen_canvas[:temp_row+1, i] == screen_canvas[:temp_row+1,temp_col-most_left ]) and condition_odd:
                        pass
                        print 'odd_most____pass' 
                    else:
                        print 'odd_most_break'
                        break
                """ middle checking """
                if i !=0 and i != (temp_col-most_left)/2:
                    if np.all(screen_canvas[:,i]==screen_canvas[:,temp_col-most_left-i]):
                        pass
                        print 'odd_middle_pass' 
                    else:
                        print  'odd_middle_break'
                        break
                if i== (temp_col-most_left)/2:
                    key= most_left
                    find_the_best=True
                    print 'odd_got_it'
                    break
                    
                    
                        
                        
        if find_the_best:
            if cmp_joint_num(canvas[:,most_left:temp_col])>= threshold:
                break
            else:
                find_the_best=False
                key=0
                
            
    return key
            