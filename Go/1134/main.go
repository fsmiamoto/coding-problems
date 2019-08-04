package main

import "fmt"

const (
	_ = iota
	alcool
	gasolina
	diesel
	fim
)

var nomes = []string{" ", "Alcool", "Gasolina", "Diesel"}

func main() {
	var escolha int
	var qntd [4]int

	for {
		fmt.Scanf("%d", &escolha)

		if escolha < 1 || escolha > 4 {
			continue
		} else if escolha == fim {
			break
		}

		switch escolha {
		case alcool:
			qntd[alcool]++
		case gasolina:
			qntd[gasolina]++
		case diesel:
			qntd[diesel]++
		}
	}

	// Apresenta resultados
	fmt.Println("MUITO OBRIGADO")
	for i := 1; i < 4; i++ {
		fmt.Printf("%s: %d\n", nomes[i], qntd[i])
	}
}
