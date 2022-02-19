package main

import (
	"fmt"
	"time"
)

func main() {
	var mes, dia int
	natal := time.Date(2016, 12, 25, 0, 0, 0, 0, time.UTC)

	for {
		_, err := fmt.Scanf("%d %d", &mes, &dia)

		if err != nil {
			break
		}

		dataAtual := time.Date(2016, time.Month(mes), dia, 0, 0, 0, 0, time.UTC)

		if dataAtual.After(natal) {
			fmt.Println("Ja passou!")
			continue
		}

		if dataAtual.Equal(natal) {
			fmt.Println("E natal!")
			continue
		}

		diasFaltantes := int(natal.Sub(dataAtual).Hours() / 24)

		if diasFaltantes == 1 {
			fmt.Println("E vespera de natal!")
			continue
		}

		fmt.Printf("Faltam %d dias para o natal!\n", diasFaltantes)
	}

}
