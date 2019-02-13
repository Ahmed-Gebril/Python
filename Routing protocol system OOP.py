class Router(object):
    """ this class is the router we eill use in this project it has its the following attributes:
    self.name:  has the name of the router 
    self.__neighbors : list of all neighbouring routers 
    self.__routing_table =  dictionary of all networks as keys and their distance to the router as value
    """

    def __init__(self, router):
        """
        initiate the name of the router , its routing table and its list of neibours to none 

        :param router:  name of the router
        :return:  nothing 
        """

        self.name = router
        self.__neighbors = []
        self.__routing_table = {}

    def add_neighbour(self, second_router):
        """
        this function adds a neighbor to the router a neighbor router's name to its neibours list.

        :param second_router:  parameter of types router 
        :return: nothing 
        """
        self.__neighbors.append(second_router.name)

    def add_network(self, str, int):
        """
        This function adds a network and its distance to the router via the attribute routing table which is a dictionary whose key 
        is the network name and the value is the distance from that router.

        :param str: network name of string type 
        :param int: the network distance from the router 
        :return: nothing 
        """
        self.__routing_table[str] = int

    def get_routing_table(self):
        """
        this function is a getter that return the routing table
        :return: the routing table of the router
        """
        return self.__routing_table

    def receive_routing_table(self, neibouring_router):
        """
        This function  adds the routing table of the neighboring router to the router 
        it checks if the network of the neighbor router is existed in the routing table of the router or not 
        if yes it add noting 
        if no it adds the network name to the routing table and increment the distance by one 
        :param self: 
        :param neibouring_router: object of router type
        :return: 
        """
        neighbor_table = neibouring_router.get_routing_table()
        for network in neighbor_table:
            if network in self.__routing_table:
                continue
            else:
                self.__routing_table[network] = neighbor_table[network] + 1

    def get_neighbours(self):
        """
        This function returns the  list of neighbors of the router 

        :return:  self.__neighbors
        """
        return self.__neighbors

    def has_route(self, network):
        """
        This function checks if the router has route to a network or not , in other sense
        it checks if the network is existed in the routing table of the router or not . 

        :param network: 
        :return: nothing 
        """

        if network in self.__routing_table.keys():
            if self.__routing_table[network] == 0:
                print('Router is an edge router for the network.')
            else:
                print('Network', network, 'is', self.__routing_table[network],
                      'hops away')
        else:
            print('Route to the network is unknown.')

    def print_info(self):
        """
        this function prints the neighboring routers and the routing table of the router  
        :param self: 
        :return: NOTHING
        """
        print(' ', self.name)
        print('    N:', ", ".join(sorted(self.__neighbors)))
        print('    R: ', end="")
        if len(self.__routing_table.keys()) > 1:
            sortedlist_network = sorted(list(self.__routing_table.keys()))
            for netowrk_name in sortedlist_network:
                if netowrk_name == sortedlist_network[-1]:
                    print(netowrk_name, ':',
                          self.__routing_table[netowrk_name], sep='')
                else:
                    print(netowrk_name, ':',
                          self.__routing_table[netowrk_name], ', ', sep='',
                          end="")
        else:
            for netowrk_name in self.__routing_table:
                print(netowrk_name, ':', self.__routing_table[netowrk_name],
                      sep='')
        print()


def main():
    routers = {}  # a dictionary of the routers that has a key which present the router
    #  name and the value represents the object itself created of type router
    routerfile = input("Network file: ")
    yahya = ''
    routerfile1 = yahya + routerfile
    if routerfile != '':

        try:
            with open(routerfile1) as file:
                allrows = file.read().splitlines()
                for row in allrows:

                    routers_and_networks = row.split(
                        '!')  # GETTING THE ROUTERS AND NETWORKS-DISTANCE IN THE ROW
                    if routers_and_networks[0] not in routers.keys():
                        routers[routers_and_networks[0]] = Router(
                            routers_and_networks[0])

                    if routers_and_networks[1] != '':
                        if ';' in routers_and_networks[1]:
                            neighbors = routers_and_networks[1].split(';')
                            for neibr in neighbors:
                                if neibr not in routers.keys():
                                    routers[neibr] = Router(neibr)
                                    routers[
                                        routers_and_networks[0]].add_neighbour(
                                        routers[neibr])
                                else:
                                    routers[
                                        routers_and_networks[0]].add_neighbour(
                                        routers[neibr])
                        else:
                            if routers_and_networks[1] not in routers.keys():
                                routers[routers_and_networks[1]] = Router(
                                    routers_and_networks[1])
                                routers[routers_and_networks[0]].add_neighbour(
                                    routers[routers_and_networks[1]])
                            else:
                                routers[routers_and_networks[0]].add_neighbour(
                                    routers[routers_and_networks[1]])
                    if routers_and_networks[
                        2] != '':  # if there is networks in the row
                        if ':' in routers_and_networks[2]:
                            network_dist = routers_and_networks[2].split(':')
                            routers[routers_and_networks[0]].add_network(
                                network_dist[0], int(network_dist[1]))
                        else:
                            print(
                                'Error: the file could not be read or there is something wrong with it.')
                            return





        except:
            print(
                'Error: the file could not be read or there is something wrong with it.')
            return

    while True:
        command = input("> ")
        command = command.upper()

        if command == "P":  # p command prints the contents of the router
            name = input('Enter router name: ')
            if name in routers.keys():
                routers[name].print_info()
            else:
                print('Router was not found.')


        elif command == "PA":  # print all the routers in the data structure
            list_routers_sorted = sorted(routers.keys())
            for router_name in list_routers_sorted:
                routers[router_name].print_info()


        elif command == "S":  # SEND the  routing table of the router to their neighbouring routers
            router_neighbours = []
            sending_router = input('Sending router: ')
            router_neighbours = routers[sending_router].get_neighbours()
            for neibour in router_neighbours:
                routers[neibour].receive_routing_table(routers[sending_router])

        elif command == "C":  # connets two routers
            first_router = input('Enter 1st router: ')
            second_router = input('Enter 2nd router: ')
            routers[first_router].add_neighbour(routers[second_router])
            routers[second_router].add_neighbour(routers[first_router])


        elif command == "RR":  # if the router has route
            router_n = input('Enter router name: ')
            network_n = input('Enter network name: ')
            routers[router_n].has_route(network_n)


        elif command == "NR":  # add new router
            router = input('Enter a new name: ')
            if router in routers.keys():
                print('Name is taken.')
            else:
                routers[router] = Router(router)




        elif command == "NN":  # add new network
            router_name = input('Enter router name: ')
            network = input('Enter network: ')
            distance = int(input('Enter distance: '))
            routers[router_name].add_network(network, distance)

        elif command == "Q":
            print("Simulator closes.")
            return

        else:
            print("Erroneous command!")
            print("Enter one of these commands:")
            print("NR (new router)")
            print("P (print)")
            print("C (connect)")
            print("NN (new network)")
            print("PA (print all)")
            print("S (send routing tables)")
            print("RR (route request)")
            print("Q (quit)")


main()