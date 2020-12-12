#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:11:03 2020

@author: ritadang
"""
#%%
import tkinter as Tk

def knights_tour(n):
    """
    The function creates the initial chessboard 
    and launch an n × n knight’s tour game.
    """ 
    root=Tk.Tk()
    KnightsTour(root,n)
    root.mainloop()
    

class KnightsTour:
    
    def __init__(self,master,n):
        self.master=master
        self.n=n
          
        #create the chessboard
        self.board=Tk.Canvas(master,width=400,height=400)
        self.board.pack()
          
        self.square_len=400/n
        
        #create vertical lines
        for i in range(1,n+1):
            self.board.create_line(self.square_len*i,0,self.square_len*i,self.square_len*n)
              
        #create horizontal lines
        for i in range(n+1):
            self.board.create_line(0,self.square_len*i,self.square_len*n,self.square_len*i)
        
        #create the starting square
        self.start=self.board.create_rectangle(0,0,self.square_len,self.square_len,fill='orange')
        self.squares=[self.start]  #a list that stores the rectangles that have been created
        self.visited=[[1,1]]  #a list of lists for storing the square coordinates that have been visited
        self.unique=[[1,1]] #a list of lists for checking whether all squares have been visited once
        
        self.board.bind("<Button-1>",self.move_squares)
  
    def move_squares(self,event):
        
        #figure out which square is clicked
        self.x=event.x/self.square_len  #x-pos in horizontal direction
        for i in range(1,self.n+1):
            if self.x<i:
                self.x=i
                #print(self.x)
                break
        self.y=event.y/self.square_len  #y-pos in vertical direction
        for i in range(1,self.n+1):
            if self.y<i:
                self.y=i
                #print(self.y)
                break
        
        
        self.previous_click=self.squares[len(self.squares)-1]
        self.previous_visit=self.visited[len(self.visited)-1]
        self.current_visit=[self.x,self.y]
        self.check(self.current_visit)
        
        
        
    def check(self,currentcoord):
        #list all the possible moves
        a1=[self.previous_visit[0]+2,self.previous_visit[1]-1]
        a2=[self.previous_visit[0]+2,self.previous_visit[1]+1]
        a3=[self.previous_visit[0]-2,self.previous_visit[1]-1]
        a4=[self.previous_visit[0]-2,self.previous_visit[1]+1]
        a5=[self.previous_visit[0]-1,self.previous_visit[1]+2]
        a6=[self.previous_visit[0]+1,self.previous_visit[1]+2]
        a7=[self.previous_visit[0]-1,self.previous_visit[1]-2]
        a8=[self.previous_visit[0]+1,self.previous_visit[1]-2] 
        #allow the user to click the currently occupied square
        a9=[self.previous_visit[0],self.previous_visit[1]]
        
        #if the user's click is allowed
        if currentcoord == a1 or currentcoord ==a2 or currentcoord ==a3 or currentcoord ==a4 or currentcoord ==a5 or currentcoord ==a6 or currentcoord ==a7 or currentcoord ==a8 or currentcoord ==a9:
            self.click=self.board.create_rectangle(self.square_len*(self.x-1),self.square_len*(self.y-1),self.square_len*self.x,self.square_len*self.y,fill='orange')
            self.update_square()
            self.squares.append(self.click)
            self.visited.append(currentcoord)
            
            not_inlist=True
            for i in range(len(self.unique)):
                if currentcoord==self.unique[i]:
                    not_inlist=False
            if not_inlist:
                self.unique.append(currentcoord)
                self.endgame()
                    
        else:
            print("This move is not allowed. Try again!")
        
    
        
    def update_square(self):
        
        self.board.itemconfig(self.previous_click,fill='blue')
        
    def endgame(self):
        if len(self.unique)==self.n*self.n:
            self.previous_click=self.squares[len(self.squares)-1]
            self.update_square()
            self.board.unbind("<Button-1>")  #disactivate button click
            print("You finished the game!")
        
        
#test cases
knights_tour(5)



