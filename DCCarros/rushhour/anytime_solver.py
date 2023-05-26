from binary_heap import BinaryHeap
from node import Node
from copy import deepcopy
import math

class Anytime:
    """
    Implementación de anytime solver

    Atributos:
    board: Configuración inicial del puzzle
    h: Heurística
    """

    def __init__(self, initial_state, expansion_limit, heuristic, weight=1):
        self.expansions = 0
        self.expansions_limits = expansion_limit
        self.generated = 0
        self.initial_state = initial_state
        self.weight = weight
        initial_state.set_heuristic(heuristic)
        self.last_cost = math.inf

    def search(self):
        self.open = BinaryHeap()
        initial_node = Node(self.initial_state)
        initial_node.g = 0
        initial_node.h = self.initial_state.heuristic()
        initial_node.key = 1000 * 1 * initial_node.h
        w = self.weight
        self.open.insert(initial_node)
        self.generated = {}
        self.generated[self.initial_state.id()] = initial_node
        while self.expansions < self.expansions_limits:
            n = self.open.extract()
            '''Hago uso de este if para poder ver si la open tiene elementos en su interior o no
            podría haberlo hecho en el while, pero creo que queda más claro así'''
            if n is None:
                yield None
            '''
            Acá veo si el nodo que estoy revisando es el objetivo, de ser el caso primero veo todos 
            los movimientos que se hicieron para poder retornarlos con yield y poder imprimirselo
            al usuario, quien luego verá si decide buscar otra solución o quedarse con ella.
            '''
            if n.state.is_goal():
                self.last_cost = n.g
                yield n
                actual_open = self.open.get_nodes() # Veo cuales son los nodos que están en la open
                minimo = math.inf
                for element in actual_open: # recorro los nodos de la open para encontrar el nuevo peso
                    if element.g + element.h < minimo:
                        minimo = element.g + element.h
                w = self.last_cost / minimo
                for element in actual_open: # actualizo los f de cada nodo en la open
                    element.key = element.g + w * element.h
                self.open.reorder()
            '''
            Con este if llevo a cabo la poda solicitada en el punto 5 de la parte 1, y lo demás no 
            cambia de la implementación de A* normal.
            '''
            if self.last_cost > n.g + n.h:
                succ = n.state.successors()
                self.expansions += 1
                for action, child_state, cost in succ:
                    child_node = self.generated.get(child_state.id())
                    is_new = child_node is None
                    path_cost = n.g + cost  # Costo del camino encontrado hasta child_state
                    if (is_new or path_cost < child_node.g):
                        """si vemos este estado por primera vez o lo vemos por
                        un mejor camino, entonces lo agregamos a open"""
                        if is_new:  # Creamos el nodo si no existe
                            child_node = Node(child_state, n)
                            child_node.h = child_state.heuristic()
                            self.generated[child_state.id()] = child_node
                        else:  # Actualizamos el padre si existe
                            child_node.parent = n
                        child_node.action = action
                        child_node.g = path_cost
                        child_node.key = child_node.g + w * child_node.h  # Actualizamos el f del child_node
                        self.open.insert(child_node)
        yield None

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