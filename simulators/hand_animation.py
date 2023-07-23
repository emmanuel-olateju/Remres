from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor

class HandAnimation(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        #load hand model
        self.hand_model = self.loader.loadModel('models/Hand.dae')
        self.hand_model.reparent_to(self.render)

        self.hand_model.setPos(0,10,0)
        self.print_node_hierarchy(self.hand_model)

    def print_node_hierarchy(self, node_path, indent=0):
        # Print the name of the current node
        print(" " * indent + node_path.getName())

        # Recursively print children nodes
        for child in node_path.getChildren():
            self.print_node_hierarchy(child, indent + 2)

hand = HandAnimation()
hand.run()