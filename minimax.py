import numpy as np
import time

class MinimaxSolver():
    
    def __init__(self, player):
        
        self.player = player;
        pass
    
    def jugada_Optima(self, state):
        
        child , _ = self.__maximize(state, -np.inf, np.inf, 4);
        return child;
    
    def __maximize(self, state, alpha, beta, dept):
        
        if state.is_terminando():
            return None, state.get_winner_points()[self.player];
        
        
        # evalular si la profundidad se ha acabado
        
        if dept == 0:
            return None
        
        max_child, max_utility = None, -np.inf
        
        for child in state.children():
            
            _ , utility = self._minimize(state, alpha, beta, dept - 1);
            
            if utility > max_utility:
                max_child, max_utility = child, utility;
            
            if max_utility >= beta:
                break;
                
            alpha = max(alpha , max_utility)
            
        return max_child, max_utility
    
    def __minimize(self, state, alpha, beta, dept):
        
        if state.is_terminando():
            return None, state.get_winner_points()[self.player];
        
        min_child, min_utility = None, np.inf
        
        for child in state.children():
            
            _ , utility = self.__maximize(state, alpha, beta, dept - 1);
            
            if utility < min_utility:
                min_child, min_utility = child, utility;
            
            if min_utility <= alpha:
                break;
                
            beta = min(beta , min_utility)
            
        return min_child, max_utility
    
    
    def children(self):
        options = self.get_available_decisions()
        children = []
        for option in options:
            child = copy.deepcopy(self)
            child.jugarFicha(option.left, option.right);
            children.append((option, child))
        return children

    def heuristic(self, player_name):
        heur = 0
        for player in self.players:
            if player.name == player_name:
                heur -= len(player.deck.cards)
            else:
                heur += len(player.deck.cards)
    return heur

        
        
    
    
    

 