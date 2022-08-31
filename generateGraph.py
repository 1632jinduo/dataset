import torch
import dgl
import pickle 
import numpy as np
start_day = 7
day_time = 48
def generate(graph_path):
    graph = pickle.load(open(graph_path,'rb+'))
    closs_flow = []
    period_flow = []
    trend_flow = []
    y = []
    for i in range(start_day*day_time*3, len(graph)):
        if i % 10 == 0:
            print("Generate:{}/{}".format(i, len(graph)))
        g1 = graph[i - 3 + 0]
        g2 = graph[i - 3 + 1]
        g3 = graph[i - 3 + 2]
        g = dgl.DGLGraph()
        e1_u, e1_v = g1.edges()
        e2_u, e2_v = g2.edges()
        e3_u, e3_v = g3.edges()
        e2_u = e2_u + 196
        e2_v = e2_v + 196
        e3_u = e3_u + 196*2
        e3_v = e3_v + 196*2
        g.add_nodes(196 * 3)
        g.ndata['feature'] = torch.cat((g1.ndata['feature'], g2.ndata['feature'], g3.ndata['feature']), 0)
        g.add_edges(e1_u, e1_v)
        g.add_edges(e2_u, e2_v)
        g.add_edges(e3_u, e3_v)
        a = torch.tensor(list(range(196)))
        b = torch.tensor(list(range(196, 196 * 2)))
        c = torch.tensor(list(range(196 * 2, 196 * 3)))
        g.add_edges(a, b)
        g.add_edges(b, c)
        closs_flow.append(g)

        g1 = graph[i - 3 * 48 + 0 * 48]
        g2 = graph[i - 3 * 48 + 1 * 48]
        g3 = graph[i - 3 * 48 + 2 * 48]
        g = dgl.DGLGraph()
        e1_u, e1_v = g1.edges()
        e2_u, e2_v = g2.edges()
        e3_u, e3_v = g3.edges()
        e2_u = e2_u + 196
        e2_v = e2_v + 196
        e3_u = e3_u + 196*2
        e3_v = e3_v + 196*2
        g.add_nodes(196 * 3)
        g.ndata['feature'] = torch.cat((g1.ndata['feature'], g2.ndata['feature'], g3.ndata['feature']), 0)
        g.add_edges(e1_u, e1_v)
        g.add_edges(e2_u, e2_v)
        g.add_edges(e3_u, e3_v)
        a = torch.tensor(list(range(196)))
        b = torch.tensor(list(range(196, 196 * 2)))
        c = torch.tensor(list(range(196 * 2, 196 * 3)))
        g.add_edges(a, b)
        g.add_edges(b, c)
        period_flow.append(g)

        g1 = graph[i - 3 * 48 * 7 + 0 * 48 * 7]
        g2 = graph[i - 3 * 48 * 7 + 1 * 48 * 7]
        g3 = graph[i - 3 * 48 * 7 + 2 * 48 * 7]
        g = dgl.DGLGraph()
        e1_u, e1_v = g1.edges()
        e2_u, e2_v = g2.edges()
        e3_u, e3_v = g3.edges()
        e2_u = e2_u + 196
        e2_v = e2_v + 196
        e3_u = e3_u + 196*2
        e3_v = e3_v + 196*2
        g.add_nodes(196 * 3)
        g.ndata['feature'] = torch.cat((g1.ndata['feature'], g2.ndata['feature'], g3.ndata['feature']), 0)
        g.add_edges(e1_u, e1_v)
        g.add_edges(e2_u, e2_v)
        g.add_edges(e3_u, e3_v)
        a = torch.tensor(list(range(196)))
        b = torch.tensor(list(range(196, 196 * 2)))
        c = torch.tensor(list(range(196 * 2, 196 * 3)))
        g.add_edges(a, b)
        g.add_edges(b, c)
        trend_flow.append(g)

        y.append(graph[i].ndata['feature']) #

    bigGraph=[closs_flow,period_flow,trend_flow,y]
    g = open('bigGraph', 'wb+')
    pickle.dump(bigGraph, g)
if __name__ == '__main__':
    print("Begin!")
    generate('glist')
    