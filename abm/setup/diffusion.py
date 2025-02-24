from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import matplotlib.pyplot as plt
import networkx as nx
import random

class Person(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.innovation_status = False
        self.threshold = 0.3

    def step(self):
        neighbors = list(self.model.G.neighbors(self.unique_id))
        adopted_neighbors = sum([1 for n in neighbors if self.model.agents[n].innovation_status])
        
        if len(neighbors) > 0 and adopted_neighbors / len(neighbors) > self.threshold:
            self.innovation_status = True

class DiffusionModel(Model):
    def __init__(self, n_agents=100, network_type="random", initial_adopters=0.1):
        super().__init__()
        self.schedule = RandomActivation(self)
        self.G = self.create_network(n_agents, network_type)
        self.robots = {}
        self.current_step = 0
        
        # Create agents
        for i in range(n_agents):
            agent = Person(i, self)
            self.robots[i] = agent
            self.schedule.add(agent)
        
        # Initialize random adopters
        num_initial = int(n_agents * initial_adopters)
        initial_adopters = random.sample(list(self.G.nodes), num_initial)
        for i in initial_adopters:
            self.robots[i].innovation_status = True
            
        self.datacollector = DataCollector(
            agent_reporters={'Adopted': 'innovation_status'}
        )

    def create_network(self, n_agents, network_type):
        if network_type == "random":
            return nx.erdos_renyi_graph(n_agents, p=0.08)
        elif network_type == "small-world":
            return nx.watts_strogatz_graph(n_agents, k=4, p=0.1)
        elif network_type == "scale-free":
            return nx.barabasi_albert_graph(n_agents, m=2)
        else:
            raise ValueError("Choose 'random', 'small-world', or 'scale-free'")

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
        adopted_agents = sum([1 for agent in self.schedule.agents if agent.innovation_status])
        print(f"Step {self.current_step}: Healthy diet adoption rate: {adopted_agents / len(self.agents):.2f}")
        self.current_step += 1

    def run_model(self, steps=50):
        for _ in range(steps):
            self.step()
        self.plot_network()

    def plot_network(self):
        pos = nx.spring_layout(self.G)
        colors = ['green' if self.agents[node].innovation_status else 'red' 
                 for node in self.G.nodes]
        nx.draw(self.G, pos, node_color=colors, node_size=150)
        plt.show()
