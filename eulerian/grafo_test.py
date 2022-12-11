import unittest
from bibgrafo.grafo_exceptions import *
# from meu_grafo_matriz_adjacencia_nao_dir import *
from meu_grafo import MeuGrafo

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1','J','C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Mel'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Mel')

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('a1', 'A', 'B')

        self.g_d2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        self.g_d2.adicionaAresta('a1', 'A', 'B')
        self.g_d2.adicionaAresta('a2', 'A', 'C')
        self.g_d2.adicionaAresta('a3', 'B', 'C')
        self.g_d2.adicionaAresta('a4', 'C', 'D')
        self.g_d2.adicionaAresta('a5', 'E', 'F')

        self.g_d3 = MeuGrafo(['Luisa','Pedro', 'Rebeca', 'Mariana', 'Gabriel', 'Augusto',
         'Leticia', 'Amanda', 'Lucas', 'Isabel'])
        self.g_d3.adicionaAresta('a1', 'Pedro', 'Mariana')
        self.g_d3.adicionaAresta('a2', 'Gabriel', 'Mariana')
        self.g_d3.adicionaAresta('a3', 'Pedro', 'Gabriel')
        self.g_d3.adicionaAresta('a4', 'Rebeca', 'Augusto')
        self.g_d3.adicionaAresta('a5', 'Augusto', 'Leticia')
        self.g_d3.adicionaAresta('a6', 'Leticia', 'Rebeca')
        self.g_d3.adicionaAresta('a7', 'Amanda', 'Lucas')
        self.g_d3.adicionaAresta('a8', 'Amanda', 'Isabel')
        self.g_d3.adicionaAresta('a9', 'Lucas', 'Isabel')

        #Grafo rede social com arestas paralelas
        self.g_pa = MeuGrafo(['Ana', 'Fabiano', 'Mel', 'Isabella', 'Carlos'])
        self.g_pa.adicionaAresta('amizade1', 'Ana', 'Carlos')
        self.g_pa.adicionaAresta('amizade2', 'Carlos', 'Ana')
        self.g_pa.adicionaAresta('amizade3', 'Isabella', 'Ana')
        self.g_pa.adicionaAresta('amizade4', 'Mel', 'Isabella')
        self.g_pa.adicionaAresta('amizade5', 'Fabiano', 'Ana')
        self.g_pa.adicionaAresta('amizade6', 'Carlos', 'Mel')
        self.g_pa.adicionaAresta('amizade7', 'Isabella', 'Fabiano')
        self.g_pa.adicionaAresta('amizade8', 'Isabella', 'Fabiano')

        # Grafos de arvores DFS para teste da função DFS
        self.g_p_dfs_j = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_dfs_j.adicionaAresta('a1', 'J', 'C')
        self.g_p_dfs_j.adicionaAresta('a2', 'C', 'E')
        self.g_p_dfs_j.adicionaAresta('a4', 'P', 'C')
        self.g_p_dfs_j.adicionaAresta('a6', 'T', 'C')
        self.g_p_dfs_j.adicionaAresta('a8', 'M', 'T')
        self.g_p_dfs_j.adicionaAresta('a9', 'T', 'Z')

        self.g_p_dfs_z = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_dfs_z.adicionaAresta('a1', 'J', 'C')
        self.g_p_dfs_z.adicionaAresta('a2', 'C', 'E')
        self.g_p_dfs_z.adicionaAresta('a4', 'P', 'C')
        self.g_p_dfs_z.adicionaAresta('a6', 'T', 'C')
        self.g_p_dfs_z.adicionaAresta('a7', 'M', 'C')
        self.g_p_dfs_z.adicionaAresta('a9', 'T', 'Z')

        self.g_p_dfs_m = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_dfs_m.adicionaAresta('a1', 'J', 'C')
        self.g_p_dfs_m.adicionaAresta('a2', 'C', 'E')
        self.g_p_dfs_m.adicionaAresta('a4', 'P', 'C')
        self.g_p_dfs_m.adicionaAresta('a6', 'T', 'C')
        self.g_p_dfs_m.adicionaAresta('a7', 'M', 'C')
        self.g_p_dfs_m.adicionaAresta('a9', 'T', 'Z')

        self.g_c_dfs_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c_dfs_c.adicionaAresta('a1','J','C')
        self.g_c_dfs_c.adicionaAresta('a2', 'J', 'E')
        self.g_c_dfs_c.adicionaAresta('a6', 'P', 'E')

        self.g_c_dfs_e = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c_dfs_e.adicionaAresta('a1','J','C')
        self.g_c_dfs_e.adicionaAresta('a2', 'J', 'E')
        self.g_c_dfs_e.adicionaAresta('a5', 'P', 'C')

        self.g_c_dfs_j = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c_dfs_j.adicionaAresta('a1','J','C')
        self.g_c_dfs_j.adicionaAresta('a4', 'E', 'C')
        self.g_c_dfs_j.adicionaAresta('a6', 'P', 'E')

        self.g_c2_dfs_nina = MeuGrafo(['Nina', 'Mel'])
        self.g_c2_dfs_nina.adicionaAresta('amiga', 'Nina', 'Mel')

        self.g_c3_dfs_j = MeuGrafo(['J'])

        # Grafos de arvores BFS para teste da função BFS
        self.g_p_bfs_j = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_bfs_j.adicionaAresta('a1', 'J', 'C')
        self.g_p_bfs_j.adicionaAresta('a2', 'C', 'E')
        self.g_p_bfs_j.adicionaAresta('a4', 'P', 'C')
        self.g_p_bfs_j.adicionaAresta('a6', 'T', 'C')
        self.g_p_bfs_j.adicionaAresta('a7', 'M', 'C')
        self.g_p_bfs_j.adicionaAresta('a9', 'T', 'Z')

        self.g_p_bfs_z = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_bfs_z.adicionaAresta('a1', 'J', 'C')
        self.g_p_bfs_z.adicionaAresta('a2', 'C', 'E')
        self.g_p_bfs_z.adicionaAresta('a4', 'P', 'C')
        self.g_p_bfs_z.adicionaAresta('a6', 'T', 'C')
        self.g_p_bfs_z.adicionaAresta('a8', 'M', 'T')
        self.g_p_bfs_z.adicionaAresta('a9', 'T', 'Z')

        self.g_p_bfs_m = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_bfs_m.adicionaAresta('a1', 'J', 'C')
        self.g_p_bfs_m.adicionaAresta('a2', 'C', 'E')
        self.g_p_bfs_m.adicionaAresta('a4', 'P', 'C')
        self.g_p_bfs_m.adicionaAresta('a7', 'M', 'C')
        self.g_p_bfs_m.adicionaAresta('a8', 'M', 'T')
        self.g_p_bfs_m.adicionaAresta('a9', 'T', 'Z')

        self.g_c_bfs_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c_bfs_c.adicionaAresta('a1','J','C')
        self.g_c_bfs_c.adicionaAresta('a4', 'E', 'C')
        self.g_c_bfs_c.adicionaAresta('a5', 'P', 'C')

        self.g_c_bfs_e = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c_bfs_e.adicionaAresta('a2', 'J', 'E')
        self.g_c_bfs_e.adicionaAresta('a4', 'E', 'C')
        self.g_c_bfs_e.adicionaAresta('a6', 'P', 'E')

        self.g_c_bfs_j = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c_bfs_j.adicionaAresta('a1','J','C')
        self.g_c_bfs_j.adicionaAresta('a2', 'J', 'E')
        self.g_c_bfs_j.adicionaAresta('a3', 'J', 'P')

        self.g_c2_bfs_nina = MeuGrafo(['Nina', 'Mel'])
        self.g_c2_bfs_nina.adicionaAresta('amiga', 'Nina', 'Mel')

        self.g_c3_bfs_j = MeuGrafo(['J'])

        self.g_g1 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
        self.g_g1.adicionaAresta("1", "A", "B")
        self.g_g1.adicionaAresta("2", "A", "G")
        self.g_g1.adicionaAresta("3", "A", "J")
        self.g_g1.adicionaAresta("4", "K", "G")
        self.g_g1.adicionaAresta("5", "K", "J")
        self.g_g1.adicionaAresta("6", "J", "G")
        self.g_g1.adicionaAresta("7", "J", "I")
        self.g_g1.adicionaAresta("8", "I", "G")
        self.g_g1.adicionaAresta("9", "G", "H")
        self.g_g1.adicionaAresta("10", "H", "F")
        self.g_g1.adicionaAresta("11", "F", "B")
        self.g_g1.adicionaAresta("12", "B", "G")
        self.g_g1.adicionaAresta("13", "B", "C")
        self.g_g1.adicionaAresta("14", "C", "D")
        self.g_g1.adicionaAresta("15", "D", "E")
        self.g_g1.adicionaAresta("16", "D", "B")
        self.g_g1.adicionaAresta("17", "E", "B")

        self.g_g2 = MeuGrafo(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.g_g2.adicionaAresta('a1', '1', '2')
        self.g_g2.adicionaAresta('a2', '2', '4')
        self.g_g2.adicionaAresta('a3', '3', '2')
        self.g_g2.adicionaAresta('a4', '2', '3')
        self.g_g2.adicionaAresta('a5', '2', '4')
        self.g_g2.adicionaAresta('a6', '2', '6')
        self.g_g2.adicionaAresta('a7', '2', '5')
        self.g_g2.adicionaAresta('a8', '5', '6')
        self.g_g2.adicionaAresta('a9', '8', '6')
        self.g_g2.adicionaAresta('a10', '7', '6')
        self.g_g2.adicionaAresta('a11', '8', '7')
        self.g_g2.adicionaAresta('a12', '8', '9')

        # Ponte de Königsberg
        self.konigsberg = MeuGrafo(["1", "2", "3", "4"])
        self.konigsberg.adicionaAresta("a1", "1", "2")
        self.konigsberg.adicionaAresta("a2", "1", "2")
        self.konigsberg.adicionaAresta("a3", "1", "3")
        self.konigsberg.adicionaAresta("a4", "1", "4")
        self.konigsberg.adicionaAresta("a5", "1", "4")
        self.konigsberg.adicionaAresta("a6", "2", "3")
        self.konigsberg.adicionaAresta("a7", "3", "4")

        # Com caminho euleriano
        self.grafo_e1 = MeuGrafo(["1","2","3","4","5","6"])
        self.grafo_e1.adicionaAresta("a1", "1", "2")
        self.grafo_e1.adicionaAresta("a2", "1", "3")
        self.grafo_e1.adicionaAresta("a3", "1", "4")
        self.grafo_e1.adicionaAresta("a4", "1", "6")
        self.grafo_e1.adicionaAresta("a5", "2", "3")
        self.grafo_e1.adicionaAresta("a6", "2", "5")
        self.grafo_e1.adicionaAresta("a7", "2", "6")
        self.grafo_e1.adicionaAresta("a8", "3", "4")
        self.grafo_e1.adicionaAresta("a9", "3", "5")
        
        self.grafo_e2 = MeuGrafo(["1","2","3","4","5","6"])
        self.grafo_e2.adicionaAresta("A", "1", "2")
        self.grafo_e2.adicionaAresta("B", "2", "5")
        self.grafo_e2.adicionaAresta("C", "4", "5")
        self.grafo_e2.adicionaAresta("D", "2", "4")
        self.grafo_e2.adicionaAresta("E", "2", "6")
        self.grafo_e2.adicionaAresta("F", "5", "6")
        self.grafo_e2.adicionaAresta("G", "5", "3")
        self.grafo_e2.adicionaAresta("H", "6", "3")
        self.grafo_e2.adicionaAresta("I", "6", "4")
        self.grafo_e2.adicionaAresta("J", "3", "4")
        self.grafo_e2.adicionaAresta("K", "1", "3")

        self.grafo_e3 = MeuGrafo(["A", "B", "C", "D", "E", "F", "G"])
        self.grafo_e3.adicionaAresta("a1", "A", "B")
        self.grafo_e3.adicionaAresta("a2", "A", "C")
        self.grafo_e3.adicionaAresta("a3", "A", "F")
        self.grafo_e3.adicionaAresta("a4", "A", "G")
        self.grafo_e3.adicionaAresta("a5", "B", "G")
        self.grafo_e3.adicionaAresta("a6", "B", "F")
        self.grafo_e3.adicionaAresta("a7", "B", "C")
        self.grafo_e3.adicionaAresta("a8", "C", "D")
        self.grafo_e3.adicionaAresta("a9", "C", "E")
        self.grafo_e3.adicionaAresta("a10", "C", "F")
        self.grafo_e3.adicionaAresta("a11", "C", "G")
        self.grafo_e3.adicionaAresta("a12", "D", "E")
        self.grafo_e3.adicionaAresta("a13", "F", "G")


    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(), ['J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z', 'M-Z'])
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), [])
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), [])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())
        self.assertFalse(self.g_pa.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)
        
        # Grafo rede social
        self.assertEqual(self.g_pa.grau('Ana'), 4)
        self.assertEqual(self.g_pa.grau('Fabiano'), 3)
        self.assertEqual(self.g_pa.grau('Isabella'), 4)
        self.assertEqual(self.g_pa.grau('Carlos'), 3)
        self.assertEqual(self.g_pa.grau('Mel'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())
        self.assertTrue(self.g_pa.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['a1']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['a7', 'a8']))
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), set(['a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), set(['a1']))
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')
        self.assertEqual(set(self.g_pa.arestas_sobre_vertice('Ana')), set(['amizade1', 'amizade2', 'amizade3', 'amizade5']))
        self.assertEqual(set(self.g_pa.arestas_sobre_vertice('Mel')), set(['amizade4', 'amizade6']))
        self.assertEqual(set(self.g_pa.arestas_sobre_vertice('Fabiano')), set(['amizade5', 'amizade7', 'amizade8']))

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_pa.eh_completo()))

    def test_dfs(self):
        self.assertEqual(self.g_p.dfs('J'), self.g_p_dfs_j)
        self.assertEqual(self.g_p.dfs('Z'), self.g_p_dfs_z)
        self.assertEqual(self.g_p.dfs('M'), self.g_p_dfs_m)
        self.assertEqual(self.g_c.dfs('C'), self.g_c_dfs_c)
        self.assertEqual(self.g_c.dfs('E'), self.g_c_dfs_e)
        self.assertEqual(self.g_c.dfs('J'), self.g_c_dfs_j)
        self.assertEqual(self.g_c2.dfs('Nina'), self.g_c2_dfs_nina)
        self.assertEqual(self.g_c3.dfs('J'), self.g_c3_dfs_j)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.dfs('Q'), MeuGrafo())

    def test_bfs(self):
        self.assertEqual(self.g_p.bfs('J'), self.g_p_bfs_j)
        self.assertEqual(self.g_p.bfs('Z'), self.g_p_bfs_z)
        self.assertEqual(self.g_p.bfs('M'), self.g_p_bfs_m)
        self.assertEqual(self.g_c.bfs('C'), self.g_c_bfs_c)
        self.assertEqual(self.g_c.bfs('E'), self.g_c_bfs_e)
        self.assertEqual(self.g_c.bfs('J'), self.g_c_bfs_j)
        self.assertEqual(self.g_c2.bfs('Nina'), self.g_c2_bfs_nina)
        self.assertEqual(self.g_c3.bfs('J'), self.g_c3_bfs_j)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.bfs('X'), MeuGrafo())

    def test_ha_ciclo(self):
        self.assertEqual(self.g_p.ha_ciclo(), ['C', 'a7', 'M', 'a8', 'T', 'a6', 'C'])
        self.assertEqual(self.g_d2.ha_ciclo(), ['A', 'a2', 'C', 'a3', 'B', 'a1', 'A'])
        self.assertEqual(self.g_d3.ha_ciclo(), ['Pedro', 'a3', 'Gabriel', 'a2', 
        'Mariana', 'a1', 'Pedro'])
        self.assertEqual(self.g_g2.ha_ciclo(), ['2', 'a7', '5', 'a8', '6', 
        'a6', '2'])
        self.assertEqual(self.g_g1.ha_ciclo(), ['A', '2', 'G', '9', 'H', '10',
         'F', '11', 'B', '1', 'A'])
        self.assertEqual(self.g_l2.ha_ciclo(), ['A', 'a3', 'B', 'a1', 'A'])
        self.assertEqual(self.g_l4.ha_ciclo(), ['D', 'a1', 'D'])
        self.assertEqual(self.g_p.ha_ciclo(), ['C', 'a7', 'M', 'a8', 'T', 'a6', 'C'])
        self.assertEqual(self.g_c.ha_ciclo(), ['J', 'a3', 'P', 'a5', 'C', 'a1', 'J'])
        self.assertEqual(self.g_c2.ha_ciclo(), False)
        self.assertEqual(self.g_c3.ha_ciclo(), False)
        self.assertEqual(self.g_pa.ha_ciclo(), ['Ana', 'amizade5', 'Fabiano',
         'amizade7', 'Isabella', 'amizade3', 'Ana'])


    def test_caminho(self):
        self.assertEqual(self.g_p.caminho(2), ['J', 'a1', 'C', 'a7', 'M'])
        self.assertEqual(self.g_p.caminho(4), ['J', 'a1', 'C', 'a7', 'M', 
        'a8', 'T', 'a9', 'Z'])
        self.assertEqual(self.g_p.caminho(8), False)
        self.assertEqual(self.g_g1.caminho(5), 
        ['A', '3', 'J', '5', 'K', '4', 'G', '9', 'H', '10', 'F'])
        self.assertEqual(self.g_g1.caminho(9), 
        ['A', '3', 'J', '5', 'K', '4', 'G', '9', 'H', '10', 'F', '11', 'B', 
        '13', 'C', '14', 'D', '15', 'E'])
        self.assertEqual(self.g_g1.caminho(12), False)
        self.assertEqual(self.g_g2.caminho(4), ['1', 'a1', '2', 'a7', '5',
        'a8', '6', 'a10', '7'])
        self.assertEqual(self.g_g2.caminho(6), ['1', 'a1', '2', 'a7', '5', 
        'a8', '6', 'a10', '7', 'a11', '8', 'a12', '9'])
        self.assertEqual(self.g_g2.caminho(7), False)
        self.assertEqual(self.g_d3.caminho(2), ['Pedro', 'a1', 'Mariana', 'a2', 'Gabriel'])
        self.assertEqual(self.g_d3.caminho(10), False)
        self.assertEqual(self.g_pa.caminho(2), ['Ana', 'amizade1', 'Carlos', 'amizade6', 'Mel'])
        self.assertEqual(self.g_pa.caminho(4), ['Ana', 'amizade1', 'Carlos', 'amizade6',
         'Mel', 'amizade4', 'Isabella', 'amizade7', 'Fabiano'])
        self.assertEqual(self.g_pa.caminho(6), False)

    def test_conexo(self):
        self.assertTrue(self.g_p.conexo())
        self.assertTrue(self.g_c.conexo())
        self.assertTrue(self.g_c2.conexo())
        self.assertTrue(self.g_c3.conexo())
        self.assertFalse(self.g_d.conexo())
        self.assertFalse(self.g_d2.conexo())
        self.assertFalse(self.g_d3.conexo())
        self.assertTrue(self.g_pa.conexo())
        self.assertTrue(self.g_p_sem_paralelas.conexo())
        self.assertTrue(self.g_l5.conexo())
        self.assertFalse(self.g_l1.conexo())
        self.assertFalse(self.g_l3.conexo())
        self.assertTrue(self.g_l4.conexo())

    def test_caminho_euleriano(self):
        self.assertFalse(self.konigsberg.caminho_euleriano())
        self.assertEqual(self.grafo_e1.caminho_euleriano(), ['1', 'a1', '2', 
        'a5', '3', 'a2', '1', 'a3', '4', 'a8', '3', 'a9', '5', 'a6', '2', 'a7',
         '6', 'a4', '1'])
        self.assertEqual(self.grafo_e2.caminho_euleriano(), ['1', 'A', '2', 
        'B', '5', 'C', '4', 'D', '2', 'E', '6', 'F', '5', 'G', '3', 'H', '6', 
        'I', '4', 'J', '3', 'K', '1'])
        self.assertFalse(self.g_p.caminho_euleriano())
        self.assertEqual(self.g_c2.caminho_euleriano(), ['Mel', 'amiga', 'Nina'])
        self.assertFalse(self.g_c.caminho_euleriano())
        self.assertEqual(self.g_g1.caminho_euleriano(), ['D', '14', 'C', '13',
         'B', '1', 'A', '2', 'G', '4', 'K', '5', 'J', '6', 'G', '9', 'H', '10',
          'F', '11', 'B', '16', 'D', '15', 'E', '17', 'B', '12', 'G', '8', 'I', 
          '7', 'J', '3', 'A'])
        self.assertFalse(self.g_g2.caminho_euleriano())
        self.assertFalse(self.g_d2.caminho_euleriano())
        self.assertEqual(self.g_pa.caminho_euleriano(), ['Carlos', 'amizade1',
         'Ana', 'amizade2', 'Carlos', 'amizade6', 'Mel', 'amizade4',
          'Isabella', 'amizade3', 'Ana', 'amizade5', 'Fabiano', 'amizade7',
           'Isabella', 'amizade8', 'Fabiano'])
        self.assertFalse(self.g_l3.caminho_euleriano())
        self.assertEqual(self.g_l2.caminho_euleriano(), ['A', 'a1', 'B', 'a2', 
        'B', 'a3', 'A'])
        self.assertFalse(self.g_d3.caminho_euleriano())
        self.assertFalse(self.g_d.caminho_euleriano())
        self.assertEqual(self.grafo_e3.caminho_euleriano(), ['A', 'a1', 'B', 
        'a5', 'G', 'a4', 'A', 'a2', 'C', 'a7', 'B', 'a6', 'F', 'a10', 'C', 
        'a8', 'D', 'a12', 'E', 'a9', 'C', 'a11', 'G', 'a13', 'F', 'a3', 'A'])