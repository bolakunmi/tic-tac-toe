def tictactoe():
    entry_list={'a':' ','b':' ','c':' ','d':' ','e':' ','f':' ','g':' ','h':' ','i':' '}    
    board_tutorial="""
                a_|_b_|_c
                d_|_e_|_f     
                g | h | i 
                """
    board_play="""
                %s_|_%s_|_%s, 
                %s_|_%s_|_%s,      
                %s | %s | %s 
                """
    
    #DPLAY DEFINITIONS
    def player_x():
        entry_list_convert=[]
        print (board_tutorial)
        val=str(input('player "X" turn:')).lower()
        while entry_list[val]==' ':
            entry_list[val]='X'      

                #conversion of dictionary keys to tuple   
            for k in entry_list.values():
                entry_list_convert.append(k)
            print (board_play%(tuple(entry_list_convert)))

            #VICTORY CHECK
            if ((entry_list['a'] == entry_list['b'] == entry_list['c']=='X')) or\
             ((entry_list['d'] == entry_list['e'] == entry_list['f']=='X')) or\
             ((entry_list['g'] == entry_list['h'] == entry_list['i']=='X')) or\
             ((entry_list['a'] == entry_list['d'] == entry_list['g']=='X')) or\
             ((entry_list['b'] == entry_list['e'] == entry_list['h']=='X')) or\
             ((entry_list['c'] == entry_list['f'] == entry_list['i']=='X')) or\
             ((entry_list['a'] == entry_list['e'] == entry_list['i']=='X')) or\
             ((entry_list['c'] == entry_list['e'] == entry_list['g']=='X')):
                print ("""player X wins!""")
                quit()
        
        if (val!=entry_list.keys()):
            print ("""              bakayaro!
                        
                no vex me ooo, pick again.  
                                                    """)


    def player_o():
        entry_list_convert=[]
        print (board_tutorial)
        val=str(input('player "O" turn:')).lower()
        while entry_list[val]==' ':
            entry_list[val]='O'      

                #conversion of dictionary keys to tuple   
            for k in entry_list.values():
                entry_list_convert.append(k)
            print (board_play%(tuple(entry_list_convert)))

            #VICTORY CHECK
            if ((entry_list['a'] == entry_list['b'] == entry_list['c']=='O'))\
            or ((entry_list['d'] == entry_list['e'] == entry_list['f']=='O'))\
            or ((entry_list['g'] == entry_list['h'] == entry_list['i']=='O'))\
            or ((entry_list['a'] == entry_list['d'] == entry_list['g']=='O'))\
            or ((entry_list['b'] == entry_list['e'] == entry_list['h']=='O'))\
            or ((entry_list['c'] == entry_list['f'] == entry_list['i']=='O'))\
            or ((entry_list['a'] == entry_list['e'] == entry_list['i']=='O'))\
            or ((entry_list['c'] == entry_list['e'] == entry_list['g']=='O')):
                print ("""player O wins!""")
                quit()
                
        
        if (val!=entry_list.keys()):
            print ("""          bakayaro!
                        
                no vex me ooo, pick again.  
                                                    """)

                    
    #GAME BEGINS
    print("""welcome to the TIC-TAC-TOE
            get ready for battle soldier!
                    HAJIME!                    
                                        """)

    player_1=str(input("who goes first? X or O?")).lower()
    while player_1=='x' or player_1=='o':
        if player_1=='x':
            while True:
                player_x()
                player_o()
                if ' ' not in entry_list.values():
                    print('it is a tie')
                    quit()
            
        elif player_1=='o':
            while True:
                player_o()
                player_x()
                if ' ' not in entry_list.values():
                    print('it is a tie')
                    quit()
            
    else:
        print('you no dey read instruction?')
    

tictactoe()