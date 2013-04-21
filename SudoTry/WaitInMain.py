import Leap, sys

controller = object
listener1 = listener2 = object

class A(Leap.Listener):
    """
    Listener 1
    """
    
    count = 0
    flag = False
    
    def on_exit(self, controller):
        """ runs on exit """
        print("exited 1")
        
    def on_frame(self, controller):
        """ called for every frame
        increments count for many frames and on 1000 frame it does some work
        """
        
        self.count += 1
        
        if self.count == 1000 :
            self.flag = True
            self.on_exit(controller)
            
        elif self.count > 1000 :
            self.flag = False
            


class B(Leap.Listener):
    """
    Listener 2
    """
    
    count = 0
    flag = False
    
    def on_exit(self, controller):
        """ runs on exit """
        
        print("exited 2")
        
    def on_frame(self, controller):
        """ called for every frame
        increments count for many frames and on 1000 frame it does some work
        """
        
        self.count += 1
        
        if self.count == 1000 :
            self.flag = True
            self.on_exit(controller)
            
        elif self.count > 1000 :
            self.flag = False 


def main():
    """
    main funtion to be run
    """
    
    global controller
    controller = Leap.Controller()
    
    global listener1
    global listener2
    listener1 = A()
    listener2 = B()
    
    controller.add_listener(listener1)
    
    ## wait till something happens
    ## Beware !! enabling this will crash the program and Leap
    #while A.flag != True:
        #print A.count
        
    print("Flag in A (expected True):", A.flag)
    controller.remove_listener(listener1)
    
    controller.add_listener(listener2)
    print("Flag in B (expected True):", B.flag)
    
    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    sys.stdin.readline()
    
    controller.remove_listener(listener2)
    
if __name__ == "__main__":
    main()
