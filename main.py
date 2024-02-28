import sys
import pygame
import random
# from setting import setting,textshow
# from self import selfoo


pygame.init()


# setting a display
scrn=pygame.display.set_mode((800,700))
width,height=pygame.display.get_window_size()
pygame.display.set_caption('algorithm Visualizer')


# setting a frame rate
fps=16
clock=pygame.time.Clock()



# class of some information
class info:
    bg_color=(120,235,215)

    def __init__(self):
        self.bg_color=(250,235,215)
        self.gradients=[
            (128,128,128)
            ,(192,192,192)
            ,(160,160,160)]
        self.rangeL=(1,100)
        self.length=21
        self.side_pads=100
        self.top_pads=300
        self.list=self.set_list(self.length)
        self.max=max(self.list)
        self.min=min(self.list)
        self.block_height=int((height-self.top_pads)/(self.max-self.min))
        self.block_width=int((width-self.side_pads)/self.length)
        # if self.block_width*self.length>=710:
        #     self.block_width=int((width-self.side_pads)/self.length)
    def setall(self):
        self.list=self.set_list(self.length)
        self.max=max(self.list)
        self.min=min(self.list)
        self.block_height=int((height-self.top_pads)/(self.max-self.min))
        self.block_width=int((width-self.side_pads)/self.length)



        
    


    
        



    def set_list(self,length):
        list=[]
        for x in range(length): 
            i=random.randint(self.rangeL[0],self.rangeL[1])
            list.append(i)
         

        return list   
class algoo(info):


    ''' a should be includeed with every sorting function 


    '''
#function to draw rectangales
    def draw(self,screen,list,pos=None,min_idx=None):
        
        pygame.draw.rect(scrn,self.bg_color,(0,self.top_pads-90,width,height+14))
        
        #3 filling screen with new color so new soutput will draw
        st_x=int(self.side_pads/2)
        for i in range(len(list)):
            x=int(self.block_width*i)+st_x
            y=height-((list[i])*self.block_height)
            # print(x,y)
            color=self.gradients[i%3]                
            pygame.draw.rect(screen,color,(x,y,self.block_width,height))
 

            
      # this particular funtion is draw rectangles in different color according to sorting selforithm
            if pos!=None and min_idx!=None:
                x=int(self.block_width*min_idx)+int(self.side_pads/2)
                y=height-(list[min_idx]*self.block_height)
                pygame.draw.rect(screen,(0,250,0),(x,y,self.block_width,height))
                x=int(self.block_width*(pos))+int(self.side_pads/2)
                y=height-(list[pos]*self.block_height)
                pygame.draw.rect(screen,(125,0,0),(x,y,self.block_width,height))
        pygame.display.update()

        
 
# function to do selection sort
    
    def Aselction(self):
        for i in range(self.length):
            min_idx=i
            for j in range(i+1,self.length):


                if self.list[min_idx]>self.list[j]:
                    min_idx=j
            self.list[i],self.list[min_idx]=self.list[min_idx],self.list[i]
            alg.draw(scrn,alg.list,i,min_idx)#providing i,min_idx to change color of these rectangles
            clock.tick(fps)
            pygame.display.update()


#funtion for bubble sort
    def Abubble(self):
        alg=self
        for i in range(alg.length):
            for j in range(alg.length-1-i):
            
                if alg.list[j]>alg.list[j+1]:
                    alg.list[j+1],alg.list[j]=alg.list[j],alg.list[j+1]
                alg.draw(scrn,alg.list,j+1,j)
                # providing i and j to change color of thes rectangles
                clock.tick(fps)
                pygame.display.update()




#making objects of class so all funvtion can be acces
inf=info()                   
alg=algoo()



scrn.fill(inf.bg_color)
pygame.display.update()



#displaying commands def
def showcommands(text,pos,rectangle,size=30):
    font = pygame.font.Font('freesansbold.ttf',size)  
    textw = font.render(text,False,(34,12,12))
    # print(textw.get_size())
    if rectangle!=(0,0):
        x=int((rectangle[0]/2)-(textw.get_width()/2)+pos[0])
        y=int((rectangle[1]/2)-(textw.get_height()/2)+pos[1])
    else:
        x=pos[0]
        y=pos[1]
        
    scrn.blit(textw,(x,y))


def showarrows(direction,points,size):
    x=(points[0],points[1])
    if direction=="right":
        y=(points[0],points[1]+size)
        z=(points[0]+size,points[1]+int(size/2))
    if direction=="up":
        y=(points[0]+size,points[1])
        z=(points[0]+int(size/2),points[1]-size)
    if direction=="left":
        y=(points[0],points[1]-size)
        z=(points[0]-size,points[1]-int(size/2))


    if direction=="down":
        y=(points[0]-size,points[1])
        z=(points[0]-int(size/2),points[1]+size)


    pygame.draw.polygon(scrn, (120,34,180), (x,y,z))
    return (x,size)

def showselfinfo(selforithm,sort):
    xc=238
    yc=150

    wc=230
    hc=50

    wid=wc
    heig=hc

    xsort=xc
    ysort=197

    arrows={
        "left":[(xc-12,yc+hc),hc],"right":[(xc+wc+10,yc),hc],
        "up":[(xsort+25,ysort+20),15]
        }
    
    

    pygame.draw.rect(scrn,(120,34,180),(xc,yc,wc,hc),3)
    showcommands(selforithm,(xc,yc),(wc,hc))
    showcommands(sort,(xsort,ysort),(wc,27),20)
    # kitems=(arrows.keys(),arrows.items())
    arrows_pos=[]
    for direc in arrows.keys():
        points=arrows[direc]
        arrowpos=showarrows(direc,points[0],points[1])
        arrows_pos.append(arrowpos)

    return arrows_pos    
        





#class of selforithms and draw function

                
                    

def arrows_check(pos,arrows_pos):  #
    for i in range(len(arrows_pos)):
        # print(pos)
        if (arrows_pos[i][0][0]>=pos[0] and arrows_pos[i][0][0]<=pos[0]+arrows_pos[i][1]) and ((arrows_pos[i][0][1]>=pos[1] and arrows_pos[i][0][1]<=pos[1]+arrows_pos[i][1])):
            return i














alg_list=dir(algoo)[:-30]

def main():
    alg.draw(scrn,alg.list)
    selforithm="selection sort"
    sort="ascending"
    showcommands("Press:R (to reset)",(25,100),(0,0))
    arrows_pos=showselfinfo(selforithm,sort)
    # print(arrows_pos)
    showcommands("Press:Enter (to start)",(400,100),(0,0))
    pygame.display.update()
    (inf.block_width)
    

       

    while True:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT or event.key==pygame.K_DOWN:
                    if inf.length>7:
                        inf.length-=1
                        inf.list=inf.set_list(inf.length)
                        alg.list=inf.list
                        alg.length=inf.length
                        alg.setall()
                        alg.draw(scrn,alg.list)
                        print("hh")
                if event.key==pygame.K_RIGHT or event.key==pygame.K_UP:
                    if inf.length<312:
                        inf.length+=1
                        inf.list=inf.set_list(inf.length)
                        alg.list=inf.list
                        alg.length=inf.length
                        alg.setall()
                        alg.draw(scrn,alg.list)
                        print("h")
                    


                elif event.key==pygame.K_r:
                    inf.length+=1
                    inf.list=inf.set_list(inf.length)
                    alg.list=inf.list
                    alg.length=inf.length
                    alg.setall()

                    # inf.list=inf.set_list(inf.length)
                    alg.draw(scrn,alg.list)
                
        
                elif event.key==pygame.K_KP_ENTER:
                     alg.Aselction()
            

                
                
                     
        clock.tick(fps)



def setting_main():

    


    

    while True:

        

        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
           

            if event.type==pygame.KEYDOWN:
                print("kk")
                if event.key==pygame.K_a:
                    print("kk")
                   
                   
                
                
                

                    
        
            
            

            
            
    
        pygame.display.update()
        clock.tick(fps)
        
       

        

    

if __name__=='__main__':
    while True:
        main()
     

# while True:
#     print(0)