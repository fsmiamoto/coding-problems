package main

import "fmt"

const (
	_ = iota
	inter
	gremio
	empate
)

const (
	_ = iota
	sim
	nao
)

var (
	numVitoriasGremio int
	numVitoriasInter  int
	numEmpates        int
)

func main() {
	for {
		resultado := getResultadoGrenal()

		switch resultado {
		case inter:
			numVitoriasInter++
		case gremio:
			numVitoriasGremio++
		case empate:
			numEmpates++
		}

		fmt.Println("Novo grenal (1-sim 2-nao)")

		var escolha int
		fmt.Scanf("%d", &escolha)

		if escolha == sim {
			continue
		} else if escolha == nao {
			break
		}

	}
	apresentaResultados()

}

func getResultadoGrenal() int {
	var golsInter, golsGremio int
	fmt.Scanf("%d %d", &golsInter, &golsGremio)
	if golsInter > golsGremio {
		return inter
	} else if golsInter < golsGremio {
		return gremio
	} else {
		return empate
	}

}

func apresentaResultados() {
	numGrenais := numEmpates + numVitoriasGremio + numVitoriasInter

	fmt.Printf("%d grenais\n", numGrenais)
	fmt.Printf("Inter:%d\n", numVitoriasInter)
	fmt.Printf("Gremio:%d\n", numVitoriasGremio)
	fmt.Printf("Empates:%d\n", numEmpates)

	if numVitoriasInter > numVitoriasGremio {
		fmt.Println("Inter venceu mais")
	} else if numVitoriasInter < numVitoriasGremio {
		fmt.Println("Gremio venceu mais")
	} else {
		fmt.Println("Nao houve vencedor")
	}
}
