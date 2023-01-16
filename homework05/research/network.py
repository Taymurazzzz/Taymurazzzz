import typing as tp
from collections import defaultdict

import community as community_louvain
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from vkapi.friends import get_mutual_for_network


def ego_network(
    user_id: tp.Optional[int] = None,
    friends: tp.List[int] = None,
) -> tp.List[tp.Tuple[int, int]]:
    """
    Построить эгоцентричный граф друзей.

    :param user_id: Идентификатор пользователя, для которого строится граф друзей.
    :param friends: Идентификаторы друзей, между которыми устанавливаются связи.
    """
    # graph = {}
    # print(friends)
    # for friend_id in tqdm(friends):
    #     print(friend_id)
    #     graph[friend_id] = get_friends_id(get_friends(friend_id))
    # g = nx.Graph(directed=False)
    # for i in graph:
    #     g.add_node(i)
    #     if graph[i] != None:
    #         for j in graph[i]:
    #             if i != j and i in friends and j in friends:
    #                 g.add_edge(i, j)
    # pos = nx.spring_layout(g)
    # nx.draw_networkx_nodes(g, pos, node_size=20)
    # nx.draw_networkx_edges(g, pos)
    # plt.show()
    graph = []
    mutual = get_mutual_for_network(source_uid=friends[0], target_uids=friends)
    for friend in mutual:
        for uid in friend["common_friends"]:
            graph.append((friend["id"], uid))

    return graph


# print(ego_network(293311193, get_friends_id(get_friends(52104206))))


def plot_ego_network(net: tp.List[tp.Tuple[int, int]]) -> None:
    graph = nx.Graph()
    graph.add_edges_from(net)
    layout = nx.spring_layout(graph)
    nx.draw(graph, layout, node_size=10, node_color="black", alpha=0.5)
    plt.title("Ego Network", size=15)
    plt.show()


def get_communities(net: tp.List[tp.Tuple[int, int]]) -> tp.Dict[int, tp.List[int]]:
    communities = defaultdict(list)
    graph = nx.Graph()
    graph.add_edges_from(net)
    partition = community_louvain.best_partition(graph)
    for uid, cluster in partition.items():
        communities[cluster].append(uid)
    return communities


def describe_communities(
    clusters: tp.Dict[int, tp.List[int]],
    friends: tp.List[tp.Dict[str, tp.Any]],
    fields: tp.Optional[tp.List[str]] = None,
) -> pd.DataFrame:
    if fields is None:
        fields = ["first_name", "last_name"]

    data = []
    for cluster_n, cluster_users in clusters.items():
        for uid in cluster_users:
            for friend in friends:
                if uid == friend["id"]:
                    data.append([cluster_n] + [friend.get(field) for field in fields])  # type: ignore
                    break
    return pd.DataFrame(data=data, columns=["cluster"] + fields)
