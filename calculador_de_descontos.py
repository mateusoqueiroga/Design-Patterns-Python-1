from descontos import Desconto_por_cinco_itens, Desconto_por_mais_quinhentos_reais, Sem_desconto

class Calculador_de_descontos(object):

    def calcula(self, orcamento):
        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_quinhentos_reais(Sem_desconto())
        ).calcula(orcamento)
        return desconto
if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item("Item - 1", 100))
    orcamento.adiciona_item(Item("Item - 2", 100))
    orcamento.adiciona_item(Item("Item - 3", 200))
    orcamento.adiciona_item(Item("Item - 4", 200))
    orcamento.adiciona_item(Item("Item - 5", 200))
    orcamento.adiciona_item(Item("Item - 6", 200))

    calculador = Calculador_de_descontos()

    desconto_calculado = calculador.calcula(orcamento)

    print('desconto calculado %s' %(desconto_calculado))


## Chain of Responsibility