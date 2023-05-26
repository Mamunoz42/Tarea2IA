from collections import deque
from copy import deepcopy
from binary_heap import BinaryHeap
from node import Node
import time

class Solver2:
    def __init__(self, initial_state, final_state):
        self.opposite_action = {
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left'
        }
        self.generated = 0 
        self.initial_state = initial_state
        self.final_state = final_state

    def search(self):
        self.start_time = time.process_time()
        self.open = deque()
        self.expansions = 0
        initial_node = Node(self.initial_state)
        initial_node.origin = self.initial_state.id()
        initial_node.g = 0
        final_node = Node(self.final_state)
        final_node.origin = self.final_state.id()
        final_node.g = 0
        self.open.append(initial_node)
        self.open.append(final_node)

        self.generated = {}
        self.generated[initial_node.state.id()] = initial_node
        self.generated[final_node.state.id()] = final_node

        while not len(self.open) == 0:
            n = self.open.popleft()

            succ = n.state.successors()
            self.expansions += 1

            for action, child_state, cost in succ:
                child_node = self.generated.get(child_state.id())
                is_new = child_node is None
                path_cost = n.g + cost
                if is_new:
                    child_node = Node(child_state, n)
                    child_node.origin = n.origin
                    self.generated[child_state.id()] = child_node
                    child_node.action = action
                    child_node.g = path_cost
                    self.open.append(child_node)
                elif child_node.origin != n.origin:
                    self.end_time = time.process_time()
                    if n.origin != self.initial_state.id():
                        n, child_node = child_node, n
                        action[1] = self.opposite_action[action[1]]
                    return self.get_path(n, action, child_node)

        return None
    
    def get_path(self, node_from_start, action, node_from_end):
        moves = []
        moves_from_start = node_from_start.trace()
        moves_from_end = node_from_end.trace()
        moves_from_end.reverse()
        moves_from_end = [[action[0], self.opposite_action[action[1]]] for action in moves_from_end]
        moves = moves_from_start + [action] + moves_from_end
        return moves

    def solution(self, board, moves):
        output = ''
        output += "; ".join(["{} {}".format(move[0], move[1]) for move in moves])
        cars = deepcopy(board.cars)
        for move in moves:
            car = [x for x in cars if x.name == move[0]][0]
            output += '\nMOVE {} {}\n'.format(move[0], move[1])
            car.move(move[1], 1)
            output += self.initial_state.prettify(cars)
        return output
